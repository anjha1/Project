from pypdf import PdfReader

# Provide the correct file path to the PDF file
pdf_path = "D:\Selfitis_A_Newer_Behavioral_Addiction_A.pdf"

# Open the PDF file
pdf = PdfReader(pdf_path)

# Extract text from the first page
page = pdf.pages[0]
text = page.extract_text()

# Print the extracted text
print(text)
