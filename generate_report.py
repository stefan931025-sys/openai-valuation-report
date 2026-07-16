import os
from fpdf import FPDF

class FinancialReportPDF(FPDF):
    def header(self):
        # Draw a subtle top accent bar
        self.set_fill_color(0, 51, 102) # Deep blue accent
        self.rect(0, 0, 210, 8, "F")
        self.set_y(15)

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(128, 128, 128)
        # Page number
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

def create_report():
    pdf = FinancialReportPDF(orientation="P", unit="mm", format="A4")
    pdf.alias_nb_pages()
    pdf.set_margins(20, 20, 20)
    pdf.add_page()
    
    # --- TITLE SECTION ---
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_text_color(0, 51, 102) # Deep blue
    pdf.multi_cell(170, 10, "THE VALUATION IMPLICATIONS OF BANK OF AMERICA'S CREDIT FACILITY TO OPENAI", align="L")
    
    pdf.set_font("Helvetica", "B", 11)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(170, 6, "A Macro-Financial and Investment Banking Analysis", ln=True)
    
    pdf.ln(4)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(170, 5, "Author: Tshepo Stefan Kotelo", ln=True)
    pdf.cell(170, 5, "Date: July 16, 2026", ln=True)
    
    # Horizontal Divider Line
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
        "On July 8, 2026, Bank of America (BofA) reversed its historically conservative lending stance "
        "and extended a milestone $520 million credit line to OpenAI. This transaction officially pushes "
        "OpenAI's total available credit facility beyond the $5 billion mark and establishes BofA as one "
        "of the company's major creditors.\n\n"
        "This analysis evaluates the dual-sided valuation implications of this transaction. For OpenAI, "
        "the credit facility represents a critical, non-dilutive liquidity runway to fund capital-intensive "
        "compute infrastructure. It protects a targeted $1 trillion IPO valuation as the company navigates "
        "a massive cash burn. For Bank of America, the credit line is a strategic relationship-pricing "
        "mechanism designed to secure a lead underwriting and advisory role in the coveted mega-IPOs "
        "of the AI 'super-cycle'."
    )
    pdf.multi_cell(170, 6, summary_text)
    pdf.ln(6)

    # --- SECTION II ---
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(170, 8, "II. METHODOLOGY, DATA SUITABILITY, AND LIMITATIONS", ln=True)
    pdf.ln(2)
    
    methodology_intro = (
        "To evaluate the capital structure and valuation trajectory of OpenAI, this study triangulates private "
        "market funding records, news reports, and investment banking league tables. To maintain the highest "
        "standards of research integrity, we explicitly define the boundaries, suitability, and limitations of "
        "these data sources below:"
    )
    pdf.set_font("Helvetica", "", 10)
    pdf.multi_cell(170, 6, methodology_intro)
    pdf.ln(4)

    # Sub-bullets
    points = [
        ("1. Granularity and Confidentiality of S-1 Filings", 
         "OpenAI confidentially submitted a draft Form S-1 registration statement to the SEC in June 2026. Because this filing is confidential, exact balance-sheet components, debt covenants, interest margins, and formal risk disclosures are shielded from public view. To circumvent this, we rely on verified historical disclosures of the company's capital history-such as its massive revolving credit facilities-to build a baseline."),
        ("2. Timeframe Adequacy and Financial Revisions", 
         "Our quantitative runway modeling operates on reported financial performance and capital injections up to July 2026. This timeline is highly adequate to capture the inflection point where OpenAI transitioned to leveraged, enterprise-scale commercialization. While these figures are subject to retrospective audit adjustments prior to the public IPO, the core ratio of rapid development costs to available credit remains structurally valid."),
        ("3. Methodological Justification of the Debt-to-Equity Proxy", 
         "To assess the true valuation impact of a $520 million credit facility on an enterprise valued near $1 trillion, we utilize high-growth tech debt-to-equity ratios as an analytical proxy. For late-stage private technology companies, traditional debt serviceability metrics (such as Debt-to-EBITDA) are analytically ineffective due to net losses from massive capital expenditures on AI chip clusters.")
    ]
    
    for title, desc in points:
        pdf.set_font("Helvetica", "B", 10)
        pdf.set_text_color(0, 51, 102)
        pdf.cell(170, 6, title, ln=True)
        pdf.set_font("Helvetica", "", 10)
        pdf.set_text_color(30, 30, 30)
        pdf.multi_cell(170, 5, desc)
        pdf.ln(3)

    pdf.add_page() # Move to Page 2 for structural neatness

    # --- SECTION III ---
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(170, 8, "III. DIVERGENT VALUATION PERSPECTIVES & RESOLUTION", ln=True)
    pdf.ln(2)
    
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(170, 6, "1. Comparative Analysis of Divergent Perspectives", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(30, 30, 30)
    perspectives = (
        "- The Non-Dilutive Runway Perspective (Optimistic): Proponents argue the credit facility is an "
        "overwhelming signal of fundamental strength. It provides OpenAI with cheap, non-dilutive working capital, "
        "allowing the firm to delay its IPO to 2027 to optimize its enterprise margins and ensure it achieves "
        "its desired $1 trillion valuation.\n\n"
        "- The Investment Banking 'Loss Leader' Perspective (Skeptical): Skeptics assert that a $520 million loan "
        "is minor relative to OpenAI's projected infrastructure spend. From this view, the loan is an aggressive "
        "relationship-pricing maneuver by Bank of America to crowd out rivals like Morgan Stanley and JPMorgan, "
        "securing lucrative lead advisory fees for the upcoming IPO."
    )
    pdf.multi_cell(170, 6, perspectives)
    pdf.ln(4)

    pdf.set_font("Helvetica", "B", 10)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(170, 6, "2. Resolution via Data Triangulation", ln=True)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(30, 30, 30)
    resolution_text = (
        "Triangulating both arguments against industry capital-market data reveals that both perspectives "
        "are valid but operate on different economic planes. The $520 million credit line is minor compared "
        "to OpenAI's overall infrastructure costs. However, its inclusion is highly significant because "
        "it serves as an official institutional seal of approval from a Tier-1 US bank, reinforcing market "
        "confidence in OpenAI's creditworthiness ahead of its listing."
    )
    pdf.multi_cell(170, 6, resolution_text)
    pdf.ln(6)

    # --- SECTION IV ---
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(170, 8, "IV. ANALYTICAL REASONING & SCENARIO ANALYSIS", ln=True)
    pdf.ln(2)
    
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(170, 6, "1. Counterfactual Framework: 'If-X-Then-Y'", ln=True)
    pdf.set_font("Helvetica", "I", 10)
    pdf.set_text_color(50, 50, 50)
    pdf.multi_cell(170, 5, "If Bank of America and peer financial institutions had not extended these non-dilutive credit facilities, then OpenAI would have been forced to either accelerate its IPO timeline into a volatile 2026 market at a valuation below its $1 trillion target, or execute another highly dilutive private equity round.")
    pdf.ln(3)
    
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(30, 30, 30)
    counterfactual_desc = (
        "Without this low-cost capital buffer, OpenAI's massive cash consumption would have rapidly "
        "depleted its liquid cash reserves. This would either lead to immediate equity dilution at "
        "a lower private valuation, or a precipitous public listing before enterprise software revenues "
        "scaled to match capacity costs, forcing a sub-$1 trillion listing."
    )
    pdf.multi_cell(170, 6, counterfactual_desc)
    pdf.ln(6)

    # --- SECTION V ---
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(170, 8, "V. EVALUATIVE CONFIDENCE & UNCERTAINTY MATRIX", ln=True)
    pdf.ln(4)

    # Table Setup
    pdf.set_font("Helvetica", "B", 8)
    pdf.set_fill_color(0, 51, 102)
    pdf.set_text_color(255, 255, 255)
    
    # Headers
    pdf.cell(50, 8, "Valuation Assessment", border=1, fill=True, align="C")
    pdf.cell(30, 8, "Confidence Level", border=1, fill=True, align="C")
    pdf.cell(45, 8, "Justifying Evidence", border=1, fill=True, align="C")
    pdf.cell(45, 8, "Primary Uncertainty", border=1, fill=True, align="C")
    pdf.ln()

    # Table Rows
    pdf.set_font("Helvetica", "", 7.5)
    pdf.set_text_color(30, 30, 30)
    
    row1 = [
        "Credit facility acts as non-dilutive runway defense for a $1T IPO.",
        "Medium-High",
        "Alignment with confidential S-1 files & delay deliberations.",
        "Opaque covenants, rates, and exact draw-down criteria."
    ]
    row2 = [
        "BofA lending is a strategic loss-leader to secure prime IPO role.",
        "High",
        "BofA's 60% market share in AI capital fundraising since 2025.",
        "Confidential underwriting fees & late shifts in rosters."
    ]
    row3 = [
        "OpenAI can support a $1T valuation purely via consumer subs.",
        "Low",
        "High compute spend proves need for massive B2B/enterprise scale.",
        "Rapid changes in hardware efficiency reducing GPU costs."
    ]

    for row in [row1, row2, row3]:
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

    pdf.ln(6)

    # --- SECTION VI & VII ---
    pdf.set_font("Helvetica", "B", 13)
    pdf.set_text_color(0, 51, 102)
    pdf.cell(170, 8, "VI. CONCLUSION", ln=True)
    pdf.ln(2)
    pdf.set_font("Helvetica", "", 10)
    pdf.set_text_color(30, 30, 30)
    conclusion_text = (
        "Bank of America's $520 million loan to OpenAI is a highly calculated, mutually beneficial transaction. "
        "For OpenAI, it secures critical operational runway, preserving its ability to defend a premium $1 trillion "
        "IPO valuation. For Bank of America, the credit line solidifies its position at the absolute forefront of "
        "Wall Street's AI investment banking super-cycle."
    )
    pdf.multi_cell(170, 6, conclusion_text)
    pdf.ln(6)

    # Divider
    pdf.set_draw_color(220, 220, 220)
    pdf.line(20, pdf.get_y(), 190, pdf.get_y())
    pdf.ln(4)

    # Disclosure
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

    # Save File
    output_filename = "OpenAI_BofA_Valuation_Analysis.pdf"
    pdf.output(output_filename)
    print(f"Success! PDF compiled cleanly as '{output_filename}'")

if __name__ == "__main__":
    create_report()
