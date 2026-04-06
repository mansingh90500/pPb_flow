/*
 * plot.C
 *
 * Comprehensive ROOT macro for J/psi vn harmonics measurement using the
 * dihadron correlation technique described in AN-12-352 (HIN-12-015).
 *
 * Analysis technique (Equation 4 from AN-12-352):
 *
 *   (1/Ntrig) * d²Npair/(dΔη dΔφ) = B(0,0) * [S(Δη,Δφ) / B(Δη,Δφ)]
 *
 * where:
 *   S(Δη,Δφ)  - same-event pair distribution (signal), normalized by Ntrig
 *   B(Δη,Δφ)  - mixed-event pair distribution (background), normalized by Ntrig
 *   B(0,0)    - mixed-event background value at Δη≈0, Δφ≈0 (pair-acceptance
 *               correction factor)
 *
 * The Fourier decomposition extracts the v2 coefficient:
 *   C(Δφ) = 1 + 2*v2*cos(2*Δφ)
 *
 * Analysis parameters:
 *   Trigger:    J/psi  4.5 < pT < 6.0 GeV/c,  1.4 < |y| < 2.4
 *   Associated: charged hadrons  0.3 < pT < 3.0 GeV/c,  |eta| < 2.4
 *   Delta-eta:  |Δη| > 1 (away-side)
 *   Mixed events: 20 random events per trigger
 *   Vertex range: |zvtx| < 15 cm
 *
 * Input:  pPbMerged_Dataset.root   (RAGHUV0/SigMix directory, pT bin 3)
 * Output: jpsi_vn_harmonics_pT3.pdf  /  jpsi_vn_harmonics_pT3.png
 */

#include <iostream>
#include <cmath>
#include "TFile.h"
#include "TDirectoryFile.h"
#include "TH1D.h"
#include "TH2D.h"
#include "TCanvas.h"
#include "TPad.h"
#include "TStyle.h"
#include "TLegend.h"
#include "TPaveText.h"
#include "TF1.h"
#include "TMath.h"
#include "TLine.h"
#include "TLatex.h"

// ---------------------------------------------------------------------------
// Helper: project a 2D histogram onto the Δφ axis for |Δη| > etaCut.
//   Both the positive (Δη > +etaCut) and negative (Δη < -etaCut) sides are
//   summed so that the result covers the full away-side in η.
// ---------------------------------------------------------------------------
static TH1D *ProjectDeltaPhi(const TH2D *h2d, double etaCut,
                              const char *name, const char *title)
{
    if (!h2d) {
        std::cerr << "[ProjectDeltaPhi] null input histogram\n";
        return nullptr;
    }

    int nPhiBins = h2d->GetNbinsY();
    double phiMin = h2d->GetYaxis()->GetXmin();
    double phiMax = h2d->GetYaxis()->GetXmax();

    TH1D *h1d = new TH1D(name, title, nPhiBins, phiMin, phiMax);
    h1d->Sumw2();

    int nEtaBins = h2d->GetNbinsX();
    for (int iph = 1; iph <= nPhiBins; ++iph) {
        double sum  = 0.0;
        double sumE2 = 0.0;
        for (int iet = 1; iet <= nEtaBins; ++iet) {
            double etaCenter = h2d->GetXaxis()->GetBinCenter(iet);
            if (std::fabs(etaCenter) > etaCut) {
                double c = h2d->GetBinContent(iet, iph);
                double e = h2d->GetBinError(iet, iph);
                sum  += c;
                sumE2 += e * e;
            }
        }
        h1d->SetBinContent(iph, sum);
        h1d->SetBinError(iph, std::sqrt(sumE2));
    }
    return h1d;
}

// ---------------------------------------------------------------------------
// Helper: return the value of a 2D histogram at the (Δη, Δφ) bin closest
//   to (0, 0) — i.e., the B(0,0) normalization factor.
// ---------------------------------------------------------------------------
static double GetB00(const TH2D *hMix)
{
    if (!hMix) return 1.0;
    int binEta = hMix->GetXaxis()->FindBin(0.0);
    int binPhi = hMix->GetYaxis()->FindBin(0.0);
    double val = hMix->GetBinContent(binEta, binPhi);
    return (val > 0.0) ? val : 1.0;
}

// ---------------------------------------------------------------------------
// Helper: apply CMS Preliminary label at top-left of the current pad
// ---------------------------------------------------------------------------
static void DrawCMSPrelim(double x = 0.12, double y = 0.93)
{
    TLatex lat;
    lat.SetNDC();
    lat.SetTextFont(61);
    lat.SetTextSize(0.042);
    lat.DrawLatex(x, y, "CMS");
    lat.SetTextFont(52);
    lat.SetTextSize(0.036);
    lat.DrawLatex(x + 0.075, y, "Preliminary");
}

// ===========================================================================
//  Main macro
// ===========================================================================
void plot()
{
    // -----------------------------------------------------------------------
    // 0.  Style
    // -----------------------------------------------------------------------
    gStyle->SetOptStat(0);
    gStyle->SetOptFit(0);
    gStyle->SetPadTickX(1);
    gStyle->SetPadTickY(1);
    gStyle->SetLegendBorderSize(1);
    gStyle->SetLegendFillColor(0);

    // -----------------------------------------------------------------------
    // 1.  Open input file
    // -----------------------------------------------------------------------
    TFile *file = TFile::Open("pPbMerged_Dataset.root", "READ");
    if (!file || file->IsZombie()) {
        std::cerr << "Error: cannot open pPbMerged_Dataset.root\n";
        return;
    }

    // -----------------------------------------------------------------------
    // 2.  Navigate RAGHUV0/SigMix
    // -----------------------------------------------------------------------
    TDirectoryFile *dirV0 = dynamic_cast<TDirectoryFile*>(file->Get("RAGHUV0"));
    if (!dirV0) {
        std::cerr << "Error: directory RAGHUV0 not found\n";
        file->Close();
        return;
    }
    TDirectoryFile *dirSigMix = dynamic_cast<TDirectoryFile*>(dirV0->Get("SigMix"));
    if (!dirSigMix) {
        std::cerr << "Error: directory RAGHUV0/SigMix not found\n";
        file->Close();
        return;
    }

    // -----------------------------------------------------------------------
    // 3.  Retrieve 2D histograms for pT bin 3 (4.5 < pT < 6.0 GeV/c)
    //     Histogram naming convention from the analyzer:
    //       hobs_sig_c2_jpsi_vs_ch_pT_3_mass_0  -- signal
    //       hobs_mix_c2_jpsi_vs_ch_pT_3_mass_0  -- mixed-event background
    // -----------------------------------------------------------------------
    TH2D *hSig2D = dynamic_cast<TH2D*>(
        dirSigMix->Get("hobs_sig_c2_jpsi_vs_ch_pT_3_mass_0"));
    TH2D *hMix2D = dynamic_cast<TH2D*>(
        dirSigMix->Get("hobs_mix_c2_jpsi_vs_ch_pT_3_mass_0"));

    if (!hSig2D || !hMix2D) {
        std::cerr << "Error: 2D signal or mixed histogram not found in SigMix\n";
        file->Close();
        return;
    }

    // Clone so we can manipulate without touching the file
    hSig2D = static_cast<TH2D*>(hSig2D->Clone("hSig2D_clone"));
    hMix2D = static_cast<TH2D*>(hMix2D->Clone("hMix2D_clone"));
    hSig2D->SetDirectory(nullptr);
    hMix2D->SetDirectory(nullptr);
    file->Close();

    // -----------------------------------------------------------------------
    // 4.  Normalization by Ntrig
    //     The analyzer already fills S and B per-trigger (divided by Ntrig).
    //     If not, the total entry count of hSig2D integral equals Ntrig.
    //     We work with the histograms as provided (already per-trigger).
    // -----------------------------------------------------------------------
    double integralSig = hSig2D->Integral();
    double integralMix = hMix2D->Integral();
    std::cout << "\n=== Input histogram integrals ===\n"
              << "  Signal  integral : " << integralSig << "\n"
              << "  Mixed   integral : " << integralMix << "\n";

    // -----------------------------------------------------------------------
    // 5.  B(0,0) -- pair-acceptance correction factor
    //     Value of the mixed-event 2D distribution at (Δη≈0, Δφ≈0)
    // -----------------------------------------------------------------------
    double B00 = GetB00(hMix2D);
    std::cout << "  B(0,0) value     : " << B00 << "\n\n";

    // -----------------------------------------------------------------------
    // 6.  Project onto Δφ for |Δη| > 1 (away-side)
    // -----------------------------------------------------------------------
    const double etaCut = 1.0;

    TH1D *hSig1D = ProjectDeltaPhi(hSig2D, etaCut,
        "hSig1D", ";#Delta#phi (rad);(1/N_{trig}) dN^{pair}/d#Delta#phi");
    TH1D *hMix1D = ProjectDeltaPhi(hMix2D, etaCut,
        "hMix1D", ";#Delta#phi (rad);(1/N_{trig}) dN^{pair}/d#Delta#phi");

    if (!hSig1D || !hMix1D) {
        std::cerr << "Error: projection failed\n";
        return;
    }

    // -----------------------------------------------------------------------
    // 7.  Per-trigger-particle associated yield (Eq. 4 from AN-12-352)
    //
    //       Y(Δφ) = B(0,0) * S(Δφ) / B(Δφ)
    //
    //     where S and B are the 1D projections already normalized by Ntrig.
    //     Error propagation:  σ_Y = Y * sqrt( (σ_S/S)² + (σ_B/B)² )
    // -----------------------------------------------------------------------
    int nBins = hSig1D->GetNbinsX();
    TH1D *hYield = static_cast<TH1D*>(hSig1D->Clone("hYield"));
    hYield->SetTitle(";#Delta#phi (rad);(1/N_{trig}) d^{2}N^{pair}/d#Delta#eta d#Delta#phi");
    hYield->Reset();

    for (int ib = 1; ib <= nBins; ++ib) {
        double S   = hSig1D->GetBinContent(ib);
        double B   = hMix1D->GetBinContent(ib);
        double eS  = hSig1D->GetBinError(ib);
        double eB  = hMix1D->GetBinError(ib);

        double Y   = 0.0;
        double eY  = 0.0;
        if (B > 0.0 && S > 0.0) {
            Y  = B00 * S / B;
            eY = Y * std::sqrt((eS / S) * (eS / S) + (eB / B) * (eB / B));
        } else if (B > 0.0) {
            // S==0 case: yield is 0 but propagate B error
            Y  = 0.0;
            eY = B00 * eS / B;
        }
        hYield->SetBinContent(ib, Y);
        hYield->SetBinError(ib, eY);
    }

    // -----------------------------------------------------------------------
    // 8.  Correlation function: C(Δφ) = S(Δφ) / [B(0,0) * B(Δφ)]
    //     (should equal 1 in the absence of correlations)
    // -----------------------------------------------------------------------
    TH1D *hCorr = static_cast<TH1D*>(hSig1D->Clone("hCorr"));
    hCorr->SetTitle(";#Delta#phi (rad);C(#Delta#phi)");
    hCorr->Reset();

    for (int ib = 1; ib <= nBins; ++ib) {
        double S   = hSig1D->GetBinContent(ib);
        double B   = hMix1D->GetBinContent(ib);
        double eS  = hSig1D->GetBinError(ib);
        double eB  = hMix1D->GetBinError(ib);

        double denom = B00 * B;
        double C     = 0.0;
        double eC    = 0.0;
        if (denom > 0.0 && S > 0.0) {
            C  = S / denom;
            eC = C * std::sqrt((eS / S) * (eS / S) + (eB / B) * (eB / B));
        } else if (denom > 0.0) {
            C  = 0.0;
            eC = eS / denom;
        }
        hCorr->SetBinContent(ib, C);
        hCorr->SetBinError(ib, eC);
    }

    // -----------------------------------------------------------------------
    // 9.  Fourier fit:  C(Δφ) = 1 + 2*v2*cos(2*Δφ)
    //     Fit parameter [0] = 2*v2, so v2 = [0]/2
    // -----------------------------------------------------------------------
    double phiMin = hCorr->GetXaxis()->GetXmin();
    double phiMax = hCorr->GetXaxis()->GetXmax();

    TF1 *fFourier = new TF1("fFourier",
        "1.0 + [0]*TMath::Cos(2.0*x)",
        phiMin, phiMax);
    fFourier->SetParameter(0, 0.05);   // initial guess for 2*v2
    fFourier->SetParName(0, "2v_{2}");
    fFourier->SetLineColor(kRed + 1);
    fFourier->SetLineWidth(2);

    hCorr->Fit(fFourier, "QR");

    double twoV2    = fFourier->GetParameter(0);
    double twoV2err = fFourier->GetParError(0);
    double v2       = twoV2 / 2.0;
    double v2err    = twoV2err / 2.0;
    double chi2     = fFourier->GetChisquare();
    int    ndf      = fFourier->GetNDF();

    std::cout << "=== Fourier fit results ===\n"
              << "  v2        = " << v2 << " +/- " << v2err << "\n"
              << "  chi2/ndf  = " << chi2 << " / " << ndf   << "\n\n";

    // -----------------------------------------------------------------------
    // 10.  Normalise 1D projections by bin width for display
    // -----------------------------------------------------------------------
    double dPhi = hSig1D->GetBinWidth(1);
    hSig1D->Scale(1.0 / dPhi);
    hMix1D->Scale(B00 / dPhi);          // scale background by B(0,0) so that
                                         // signal ≈ background in a flat region
    hYield->Scale(1.0 / dPhi);

    // -----------------------------------------------------------------------
    // 11.  Build 4-panel canvas
    // -----------------------------------------------------------------------
    TCanvas *canvas = new TCanvas("canvas",
        "J/#psi v_{n} Harmonics Measurement (AN-12-352 technique)", 900, 1100);
    canvas->Divide(1, 4, 0.0, 0.0);

    // Shared axis label sizes
    const double labelSize  = 0.055;
    const double titleSize  = 0.058;
    const double titleOffX  = 0.85;
    const double titleOffY  = 0.90;

    // ------- Panel 1: Signal vs. Background (raw 1D projections) --------
    canvas->cd(1);
    gPad->SetLeftMargin(0.14);
    gPad->SetRightMargin(0.04);
    gPad->SetTopMargin(0.12);
    gPad->SetBottomMargin(0.02);

    hSig1D->SetLineColor(kBlack);
    hSig1D->SetMarkerColor(kBlack);
    hSig1D->SetMarkerStyle(20);
    hSig1D->SetMarkerSize(0.7);
    hSig1D->SetLineWidth(2);
    hSig1D->GetXaxis()->SetLabelSize(0.0);
    hSig1D->GetYaxis()->SetTitle("(1/N_{trig}) dN^{pair}/d#Delta#phi");
    hSig1D->GetYaxis()->SetTitleSize(titleSize * 0.85);
    hSig1D->GetYaxis()->SetTitleOffset(titleOffY * 1.1);
    hSig1D->GetYaxis()->SetLabelSize(labelSize * 0.9);
    hSig1D->Draw("E1");

    hMix1D->SetLineColor(kRed + 1);
    hMix1D->SetMarkerColor(kRed + 1);
    hMix1D->SetMarkerStyle(21);
    hMix1D->SetMarkerSize(0.7);
    hMix1D->SetLineWidth(2);
    hMix1D->SetLineStyle(2);
    hMix1D->Draw("E1 SAME");

    TLegend *leg1 = new TLegend(0.55, 0.65, 0.93, 0.87);
    leg1->SetTextSize(0.044);
    leg1->AddEntry(hSig1D, "Signal  S(#Delta#phi)", "ep");
    leg1->AddEntry(hMix1D, "Background  B(0,0)#timesB(#Delta#phi)", "ep");
    leg1->Draw();

    // analysis-parameter box
    TPaveText *infoBox = new TPaveText(0.15, 0.55, 0.52, 0.87, "NDC");
    infoBox->SetFillColor(0);
    infoBox->SetBorderSize(1);
    infoBox->SetTextSize(0.040);
    infoBox->SetTextAlign(12);
    infoBox->AddText("pPb  #sqrt{s_{NN}} = 8.16 TeV");
    infoBox->AddText("4.5 < p_{T}^{J/#psi} < 6.0 GeV/c");
    infoBox->AddText("1.4 < |y^{J/#psi}| < 2.4");
    infoBox->AddText("0.3 < p_{T}^{assoc} < 3.0 GeV/c");
    infoBox->AddText("|#Delta#eta| > 1 (away-side)");
    infoBox->AddText(Form("B(0,0) = %.4f", B00));
    infoBox->Draw();

    DrawCMSPrelim(0.14, 0.94);

    // ------- Panel 2: Per-trigger-particle associated yield ---------------
    canvas->cd(2);
    gPad->SetLeftMargin(0.14);
    gPad->SetRightMargin(0.04);
    gPad->SetTopMargin(0.01);
    gPad->SetBottomMargin(0.02);

    hYield->SetLineColor(kBlue + 1);
    hYield->SetMarkerColor(kBlue + 1);
    hYield->SetMarkerStyle(20);
    hYield->SetMarkerSize(0.7);
    hYield->SetLineWidth(2);
    hYield->GetXaxis()->SetLabelSize(0.0);
    hYield->GetYaxis()->SetTitle("(1/N_{trig}) d^{2}N^{pair}/d#Delta#eta d#Delta#phi");
    hYield->GetYaxis()->SetTitleSize(titleSize * 0.75);
    hYield->GetYaxis()->SetTitleOffset(titleOffY * 1.3);
    hYield->GetYaxis()->SetLabelSize(labelSize * 0.9);
    hYield->Draw("E1");

    TLegend *leg2 = new TLegend(0.50, 0.75, 0.93, 0.90);
    leg2->SetTextSize(0.044);
    leg2->AddEntry(hYield,
        "Y(#Delta#phi) = B(0,0)#timesS/#hat{B}", "ep");
    leg2->Draw();

    // ------- Panel 3: Correlation function C(Δφ) -------------------------
    canvas->cd(3);
    gPad->SetLeftMargin(0.14);
    gPad->SetRightMargin(0.04);
    gPad->SetTopMargin(0.01);
    gPad->SetBottomMargin(0.02);

    hCorr->SetLineColor(kGreen + 2);
    hCorr->SetMarkerColor(kGreen + 2);
    hCorr->SetMarkerStyle(20);
    hCorr->SetMarkerSize(0.7);
    hCorr->SetLineWidth(2);
    hCorr->GetXaxis()->SetLabelSize(0.0);
    hCorr->GetYaxis()->SetTitle("C(#Delta#phi) = S / [B(0,0)#timesB]");
    hCorr->GetYaxis()->SetTitleSize(titleSize * 0.82);
    hCorr->GetYaxis()->SetTitleOffset(titleOffY * 1.2);
    hCorr->GetYaxis()->SetLabelSize(labelSize * 0.9);
    hCorr->Draw("E1");

    // Baseline at C = 1
    TLine *baseLine = new TLine(phiMin, 1.0, phiMax, 1.0);
    baseLine->SetLineColor(kGray + 2);
    baseLine->SetLineStyle(2);
    baseLine->SetLineWidth(2);
    baseLine->Draw();

    TLegend *leg3 = new TLegend(0.50, 0.78, 0.93, 0.90);
    leg3->SetTextSize(0.044);
    leg3->AddEntry(hCorr,    "C(#Delta#phi)", "ep");
    leg3->AddEntry(baseLine, "Baseline  C = 1", "l");
    leg3->Draw();

    // ------- Panel 4: Fourier fit with v2 extraction ----------------------
    canvas->cd(4);
    gPad->SetLeftMargin(0.14);
    gPad->SetRightMargin(0.04);
    gPad->SetTopMargin(0.01);
    gPad->SetBottomMargin(0.14);

    TH1D *hCorrFit = static_cast<TH1D*>(hCorr->Clone("hCorrFit"));
    hCorrFit->SetTitle("");
    hCorrFit->GetXaxis()->SetTitle("#Delta#phi (rad)");
    hCorrFit->GetXaxis()->SetTitleSize(titleSize);
    hCorrFit->GetXaxis()->SetTitleOffset(titleOffX);
    hCorrFit->GetXaxis()->SetLabelSize(labelSize);
    hCorrFit->GetYaxis()->SetTitle("C(#Delta#phi)");
    hCorrFit->GetYaxis()->SetTitleSize(titleSize);
    hCorrFit->GetYaxis()->SetTitleOffset(titleOffY);
    hCorrFit->GetYaxis()->SetLabelSize(labelSize);
    hCorrFit->Draw("E1");

    fFourier->Draw("SAME");
    baseLine->Draw();

    // Fit-result text box
    TPaveText *fitBox = new TPaveText(0.15, 0.55, 0.60, 0.90, "NDC");
    fitBox->SetFillColor(0);
    fitBox->SetBorderSize(1);
    fitBox->SetTextSize(0.046);
    fitBox->SetTextAlign(12);
    fitBox->AddText("Fourier decomposition:");
    fitBox->AddText("C(#Delta#phi) = 1 + 2v_{2}cos(2#Delta#phi)");
    fitBox->AddText(Form("v_{2} = %.4f #pm %.4f", v2, v2err));
    fitBox->AddText(Form("#chi^{2}/ndf = %.2f / %d", chi2, ndf));
    fitBox->Draw();

    TLegend *leg4 = new TLegend(0.50, 0.75, 0.93, 0.90);
    leg4->SetTextSize(0.044);
    leg4->AddEntry(hCorrFit, "C(#Delta#phi)", "ep");
    leg4->AddEntry(fFourier, "Fourier fit", "l");
    leg4->Draw();

    // -----------------------------------------------------------------------
    // 12.  Save output
    // -----------------------------------------------------------------------
    canvas->Update();
    canvas->SaveAs("jpsi_vn_harmonics_pT3.pdf");
    canvas->SaveAs("jpsi_vn_harmonics_pT3.png");

    std::cout << "=== Output files ===\n"
              << "  jpsi_vn_harmonics_pT3.pdf\n"
              << "  jpsi_vn_harmonics_pT3.png\n\n";

    // -----------------------------------------------------------------------
    // 13.  Summary
    // -----------------------------------------------------------------------
    std::cout << "=== Analysis summary ===\n"
              << "  Data file         : pPbMerged_Dataset.root\n"
              << "  Directory         : RAGHUV0/SigMix\n"
              << "  pT bin 3          : 4.5 < pT < 6.0 GeV/c\n"
              << "  Δη selection      : |Δη| > " << etaCut << "\n"
              << "  Signal integral   : " << integralSig << "\n"
              << "  Mixed integral    : " << integralMix << "\n"
              << "  B(0,0)            : " << B00 << "\n"
              << "  v2                : " << v2 << " +/- " << v2err << "\n"
              << "  chi2/ndf          : " << chi2 << " / " << ndf << "\n";
}
