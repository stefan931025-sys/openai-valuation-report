import os
from fpdf import FPDF

class FinancialReportPDF(FPDF):
    def header(self):
        self.set_fill_color(0, 51, 102) # Deep blue academic banner
        self.rect(0, 0, 210, 8, "F")
        self.set_y(15)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

def create_report():
    pdf = FinancialReportPDF(orientation="P", unit="mm", format="A4")
    pdf.alias_nb_pages()
    pdf.set_margins(20, 20, 20)
    pdf.add_page()
    
    # --- TITLE SECTION ---
    pdf.set_font("Helvetica", "B", 16)
    pdf.set_text_color(0, 51, 102)
    pdf.multi_cell(170, 8, "EVALUATING THE SYSTEMIC EFFICACY OF THE RBI'S 2026 SPECIAL SWAP-BACKED FCNR(B) DEPOSIT MOBILISATION SCHEME", align="L")
    
    pdf.set_font("Helvetica", "B", 10.5)
    pdf.set_text_color(100, 100, 100)
    pdf.multi_cell(170, 5, "A Quantitative Macro-Financial Analysis of Onshore Forward Premium Subsidization, Capital Inflows, and Balance-of-Payments Efficacy", align="L")
    
    pdf.ln(4)
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(170, 4, "Author: Tshepo Stefan Kotelo", ln=True)
    pdf.cell(170, 4, "Date: July 17, 2026", ln=True)
    
    # Divider
    pdf.set_draw_color(200, 200, 200)
    pdf.line(20, pdf.get_y() + 4, 190, pdf.get_y() + 4)
    pdf.ln(8)

    # --- SECTION I ---
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(170, 6, "I. EXECUTIVE SUMMARY", ln=True)
    pdf.ln(2)
    
    pdf.set_font("Helvetica", "", 9.5)
    pdf.set_text_color(30, 30, 30)
    summary_text = (
        "In June 2026, acute geopolitical volatility in West Asia triggered a supply-side shock, pushing Brent crude "
        "toward $95/bbl and exerting structural depreciation pressure on the Indian Rupee (INR). In response, the Reserve Bank "
        "of India (RBI) instituted an emergency Foreign Currency Non-Resident Bank [FCNR(B)] concessional swap window. "
        "By offering commercial banks a direct USD/INR swap at par for 3-to-5-year term deposits, the RBI effectively "
        "absorbs 100% of open-market currency hedging costs. This brief evaluates the macroeconomic mechanics of this "
        "intervention, which successfully mobilized $10 billion in its initial weeks, assessing its sustainability against "
        "hawkish Federal Reserve monetary guidance and tightening offshore USD funding conditions."
    )
    pdf.multi_cell(170, 5.5, summary_text)
    pdf.ln(5)

    # --- SECTION II ---
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(170, 6, "II. MECHANISTIC DESIGN & RESEARCH INTEGRITY", ln=True)
    pdf.ln(2)
    
    mechanics_text = (
        "This empirical analysis models the facility against the historical precedent of the 2013 Rajan-era FCNR(B) "
        "swap window, which successfully attracted $34 billion in emergency capital. Under standard market conditions, "
        "domestic commercial banks face a steep forward-premium drag (historically annualized at 3.5%-5.0%) when converting "
        "offshore USD liabilities into domestic INR assets. The 2026 framework bypasses open-market forward swap books completely. "
        "By allowing banks to swap mobilized USD with the central bank at a fixed par rate, net hedging costs drop to 0%. "
        "This structural subsidy allows Indian commercial banks to bypass domestic deposit rate caps and offer highly competitive "
        "yields to the diaspora without compressing their net interest margins (NIMs)."
    )
    pdf.multi_cell(170, 5.5, mechanics_text)
    pdf.ln(5)

    # --- SECTION III ---
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(170, 6, "III. QUANTITATIVE MACRO PERSPECTIVES & SYSTEMIC RISK", ln=True)
    pdf.ln(2)
    
    perspectives = (
        "- Optimistic Perspective (Monetary Shield): Proponents demonstrate that the facility provides a non-inflationary, "
        "balance-of-payments (BOP) cushion. It rapidly aggregates sticky, multi-year FX reserves, allowing the RBI to "
        "sterilize capital inflows and defend the rupee without burning through its organic foreign exchange reserves "
        "via spot-market interventions.\n\n"
        "- Skeptical Perspective (Funding Dislocation): Critics note that suspending interest rate ceilings on diaspora "
        "deposits triggers aggressive domestic rate competition. Concurrently, heightened global macro risk has driven the cost "
        "of offshore leveraged investor funding up by 25-40 basis points, creating structural pricing distortions relative "
        "to domestic MIBOR-linked corporate credit."
    )
    pdf.multi_cell(170, 5.5, perspectives)
    
    pdf.add_page() # Page Break to match original layout

    # --- SECTION IV ---
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(170, 6, "IV. COUNTERFACTUAL ANALYSIS & TRADING IMPACT", ln=True)
    pdf.ln(2)
    
    pdf.set_font("Helvetica", "I", 9.5)
    pdf.set_text_color(50, 50, 50)
    pdf.multi_cell(170, 5, "Counterfactual Baseline: Absent this concessional facility, domestic commercial banks would have faced severe outward capital flight toward higher-yielding US Treasury instruments (SOFR > 5.0%). To defend the currency from breaking major psychological support levels, the RBI would have been forced into aggressive, direct spot-FX liquidation, causing systemic contractions in domestic banking liquidity and flattening the IGB yield curve prematurely.")
    pdf.ln(4)

    # --- SECTION V (TABLE) ---
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(170, 6, "V. EVALUATIVE CONFIDENCE & UNCERTAINTY MATRIX", ln=True)
    pdf.ln(3)

    # Table headers
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_fill_color(0, 51, 102)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(50, 7, "Assessment", border=1, fill=True, align="C")
    pdf.cell(25, 7, "Confidence", border=1, fill=True, align="C")
    pdf.cell(50, 7, "Quantitative Evidence", border=1, fill=True, align="C")
    pdf.cell(45, 7, "Primary Macro Risk", border=1, fill=True, align="C")
    pdf.ln()

    # Table Rows
    pdf.set_font("Helvetica", "", 7.5)
    pdf.set_text_color(30, 30, 30)
    
    rows = [
        ["Inflow Velocity: Target $50B total accumulation.", "Medium-Low", "Initial run-rate hit $10B but velocity decelerated under tight offshore USD supply.", "Federal Reserve dot plot hawkish shift; prolonged West Asia conflict."],
        ["FX Stabilization: Cushion balance-of-payments.", "High", "Subsidized forward book absorbed $10B in capital, preventing spot market drain.", "Trade deficit breakdown if Brent crude breaches $95/bbl permanently."],
        ["Banking NIMs: Insulate lender balance sheets.", "Medium-High", "Elimination of 400+ bps forward hedging premium preserves domestic net interest margins.", "Unregulated domestic price wars as banks aggressively bid for diaspora assets."]
    ]

    for row in rows:
        x_start = pdf.get_x()
        y_start = pdf.get_y()
        pdf.multi_cell(50, 4, row[0], border=1)
        pdf.set_xy(x_start + 50, y_start)
        pdf.multi_cell(25, 4, row[1], border=1, align="C")
        pdf.set_xy(x_start + 75, y_start)
        pdf.multi_cell(50, 4, row[2], border=1)
        pdf.set_xy(x_start + 125, y_start)
        pdf.multi_cell(45, 4, row[3], border=1)
        pdf.ln(1.5)

    pdf.ln(3)

    # --- SECTION VI ---
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(170, 6, "VI. POLICY RECONCILIATION & RELEVANCE", ln=True)
    pdf.ln(2)
    pdf.set_font("Helvetica", "", 9.5)
    pdf.multi_cell(170, 5.5, "The special FCNR(B) swap window represents a highly efficient tactical volatility shield, but it is not a structural substitute for long-term balance-of-payments stability. From an investment perspective, while it actively limits tail-risk depreciation for the Rupee and stabilizes short-term banking sector liquidity, relying on highly rate-sensitive diaspora inflows creates a cyclical refinancing overhang. Long-term macro stability remains contingent on structural Foreign Direct Investment (FDI) reforms rather than subsidized, hot-money liabilities.")
    pdf.ln(5)

    # Divider
    pdf.set_draw_color(220, 220, 220)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(3)

    # --- SECTION VII: AI DISCLOSURE ---
    pdf.set_font("Helvetica", "B", 8.5)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(170, 4, "VII. AI DISCLOSURE STATEMENT", ln=True)
    pdf.set_font("Helvetica", "I", 8)
    disclosure_text = (
        "This academic and financial analysis paper was prepared by the author utilizing AI-assisted collaborative "
        "research tools (specifically Gemini) for editorial refinement, structural formatting, proofreading, and "
        "financial data verification. All core analytical claims, financial valuations, and strategic interpretations "
        "remain the sole intellectual property of the author."
    )
    pdf.multi_cell(170, 4, disclosure_text)

    output_filename = "RBI_Overseas_Deposit_Scheme_Analysis_With_Disclosure.pdf"
    pdf.output(output_filename)

if __name__ == "__main__":
    create_report()
