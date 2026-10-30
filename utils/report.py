from reportlab.pdfgen import canvas

def create_pdf(name,email,phone,score):

    pdf=canvas.Canvas("reports/Resume_Report.pdf")

    pdf.setTitle("Resume Report")

    pdf.drawString(100,800,"AI Resume Analyzer")

    pdf.drawString(100,760,f"Name : {name}")

    pdf.drawString(100,730,f"Email : {email}")

    pdf.drawString(100,700,f"Phone : {phone}")

    pdf.drawString(100,670,f"Resume Score : {score}")

    pdf.save()

    return "reports/Resume_Report.pdf"