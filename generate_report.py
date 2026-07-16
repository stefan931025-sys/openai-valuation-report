import os
from fpdf import FPDF

class FinancialReportPDF(FPDF):
    def header(self):
        self.set_fill_color(0, 51, 102)
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
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(0, 51, 102)
    pdf.multi_cell(170, 10, "EVALUATING THE SYSTEMIC EFFICACY OF THE RBI'S 2026 SPECIAL SWAP-BACKED FCNR(B) DEPOSIT MOBILISATION SCHEME", align="L")
    
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(170, 6, "A Critical Macro-Financial Analysis of Rupee Stabilization", ln=True)
    
    pdf.ln(4)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(170, 5, "Author: Tshepo Stefan Kotelo", ln=True)
    pdf.cell(170, 5, "Date: July 17, 2026", ln=True)
    
    # Divider
    pdf.set_draw_color(200, 200, 200)
    pdf.line(20, pdf.get_y() + 5, 190, pdf.get_y() + 5)
    pdf.ln(10)

    # --- SECTION I ---
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(170, 8, "I. EXECUTIVE SUMMARY", ln=True)
    pdf.ln(2)
    
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(30, 30, 30)
    summary_text = (
        "In June 2026, amid escalating geopolitical tensions in West Asia and surging global crude oil prices, "
        "the Reserve Bank of India (RBI) introduced a targeted Foreign Currency Non-Resident Bank [FCNR(B)] swap window. "
        "The mechanism offers commercial banks a direct US Dollar-Rupee swap at par for 3-to-5-year term deposits mobilised "
        "from the Non-Resident Indian (NRI) diaspora, absorbing 100% of the currency hedging costs. This analysis evaluates "
        "the economic efficacy of this scheme, which successfully mobilised close to $10 billion within its initial weeks "
        "but faces mounting headwinds as rising global bond yields and US monetary tightness raise the cost of offshore funding."
    )
    pdf.multi_cell(170, 6, summary_text)
    pdf.ln(6)

    # --- SECTION II ---
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(170, 8, "II. MECHANISTIC DESIGN & RESEARCH INTEGRITY", ln=True)
    pdf.ln(2)
    
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(30, 30, 30)
    mechanics_text = (
        "To evaluate this framework, this study relies on real-time central bank announcements, commercial rate-ceiling "
        "suspensions, and empirical balance-of-payments data. The core mechanism is structurally designed to address the "
        "hedging cost bottleneck. Historically, commercial banks seeking foreign currency deposits faced substantial forward-premium "
        "hedging expenses to cover the exchange-rate risk of converting USD deposits into domestic lending. The 2026 scheme "
        "bypasses this: lenders swap foreign currency directly with the RBI at par, effectively reducing net hedging costs to 0%."
    )
    pdf.multi_cell(170, 6, mechanics_text)
    pdf.ln(6)

    # --- SECTION III ---
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(170, 8, "III. DIVERGENT MACRO PERSPECTIVES", ln=True)
    pdf.ln(2)
    
    perspectives = (
        "- Perspective A (Optimistic): Proponents argue that the special swap window is an exceptionally efficient, "
        "non-inflationary shield for the Indian rupee. By mobilizing sticky, long-term NRI capital, the central bank "
        "rapidly builds its foreign exchange reserves without relying on direct open-market intervention.\n\n"
        "- Perspective B (Skeptical): Conversely, critics highlight that suspending interest rate ceilings forces banks "
        "into an aggressive deposit-rate price war. Tight global liquidity and the West Asia conflict drive up offshore "
        "costs of leveraged structures by 25-40 basis points, dampening long-term viability."
    )
    pdf.multi_cell(170, 6, perspectives)
    
    pdf.add_page() # Move to page 2

    # --- SECTION IV ---
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(170, 8, "IV. COUNTERFACTUAL ANALYSIS", ln=True)
    pdf.ln(2)
    
    pdf.set_font("Helvetica", "I", 10)
    pdf.set_text_color(50, 50, 50)
    pdf.multi_cell(170, 5, "If the RBI had not implemented the concessional swap facility, then domestic commercial banks would have been unable to compete with high-yielding US Dollar deposits, forcing the RBI to actively defend the rupee via direct spot-market sales.")
    pdf.ln(3)

    # --- SECTION V (TABLE) ---
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(170, 8, "V. EVALUATIVE CONFIDENCE & UNCERTAINTY MATRIX", ln=True)
    pdf.ln(4)

    # Table headers
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_fill_color(0, 51, 102)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(50, 8, "Assessment", border=1, fill=True, align="C")
    pdf.cell(30, 8, "Confidence", border=1, fill=True, align="C")
    pdf.cell(45, 8, "Evidence", border=1, fill=True, align="C")
    pdf.cell(45, 8, "Primary Uncertainty", border=1, fill=True, align="C")
    pdf.ln()

    # Table Rows
    pdf.set_font("Helvetica", "", 7.5)
    pdf.set_text_color(30, 30, 30)
    
    rows = [
        ["Inflow Efficacy: Will mobilize $50-70B by Sept.", "Medium-Low", "Initial $10B has cooled due to tight offshore liquidity.", "West Asia conflict duration and Fed rate path."],
        ["Rupee Defense: Concessional swap cushions INR.", "High", "Capital absorption protected BOP during July volatility.", "Trade deficit if oil breaches $95/barrel."],
        ["Bank NIMs: Hedging sops protect margins.", "Medium-High", "Elimination of standard forward premium swap-back costs.", "Local price wars as banks compete on rates."]
    ]

    for row in rows:
        x_start = pdf.get_x()
        y_start = pdf.get_y()
        pdf.multi_cell(50, 4, row[0], border=1)
        pdf.set_xy(x_start + 50, y_start)
        pdf.multi_cell(30, 4, row[1], border=1, align="C")
        pdf.set_xy(x_start + 80, y_start)
        pdf.multi_cell(45, 4, row[2], border=1)
        pdf.set_xy(x_start + 125, y_start)
        pdf.multi_cell(45, 4, row[3], border=1)
        pdf.ln(2)

    pdf.ln(4)

    # --- SECTION VI ---
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(170, 8, "VI. POLICY RECONCILIATION & CONCLUSION", ln=True)
    pdf.ln(2)
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(170, 5.5, "The special FCNR(B) swap window is a tactical volatility shield, but not a structural panacea. It must be paired with long-term FDI enhancements rather than volatile, rate-sensitive diaspora deposits.")
    pdf.ln(6)

    # Divider
    pdf.set_draw_color(220, 220, 220)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(4)

    # --- SECTION VII: AI DISCLOSURE ---
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(170, 5, "VII. AI DISCLOSURE STATEMENT", ln=True)
    pdf.set_font("Helvetica", "I", 8.5)
    disclosure_text = (
        "This academic and financial analysis paper was prepared by the author utilizing AI-assisted collaborative "
        "research tools (specifically Gemini) for editorial refinement, structural formatting, proofreading, and "
        "financial data verification. All core analytical claims, financial valuations, and strategic interpretations "
        "remain the sole intellectual property of the author."
    )
    pdf.multi_cell(170, 4.5, disclosure_text)

    output_filename = "RBI_Overseas_Deposit_Scheme_Analysis_With_Disclosure.pdf"
    pdf.output(output_filename)

if __name__ == "__main__":
    create_report()
