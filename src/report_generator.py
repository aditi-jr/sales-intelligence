from fpdf import FPDF
from datetime import datetime
import os

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'Executive Sales Intelligence Report', 0, 1, 'C')
        self.set_font('Arial', 'I', 10)
        self.cell(0, 10, f'Generated on: {datetime.now().strftime("%Y-%m-%d %H:%M")}', 0, 1, 'C')
        self.ln(10)

def generate_executive_pdf(kpis, report_path="reports/monthly_executive_report.pdf"):
    # Ensure the reports directory exists
    os.makedirs(os.path.dirname(report_path), exist_ok=True)
    
    pdf = PDFReport()
    pdf.add_page()
    pdf.set_font('Arial', '', 12)
    
    pdf.cell(0, 10, 'Key Performance Indicators (KPIs)', 0, 1, 'L')
    pdf.set_font('Arial', '', 10)
    pdf.cell(0, 10, f"- Total Revenue: INR {kpis['Total_Revenue']:,.2f}", 0, 1)
    pdf.cell(0, 10, f"- Total Units Sold: {kpis['Total_Units_Sold']}", 0, 1)
    pdf.cell(0, 10, f"- Avg Daily Revenue: INR {kpis['Average_Daily_Revenue']:,.2f}", 0, 1)
    
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(0, 10, 'Automated Insights', 0, 1, 'L')
    pdf.set_font('Arial', '', 10)
    pdf.multi_cell(0, 10, "Data processing and anomaly detection complete. The 30-day forecast provides a baseline projection based on historical daily averages. Recommend monitoring high-value electronics to ensure sustained revenue growth.")
    
    pdf.output(report_path)
    return report_path