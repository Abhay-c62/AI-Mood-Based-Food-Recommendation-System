from reportlab.pdfgen import canvas

def generate_pdf(mood, foods):

    pdf = canvas.Canvas("Food_Recommendation.pdf")

    pdf.drawString(100,800,f"Detected Mood : {mood}")

    y=760

    for food in foods:

        pdf.drawString(
            100,
            y,
            f"{food['Food']} - {food['Calories']} Calories"
        )

        y-=25

    pdf.save()