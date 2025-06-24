from doctr.models import ocr_predictor
from doctr.io import DocumentFile

# Load your sample PDF (replace with your path if needed)
pdf_path = "sample.pdf"

# Load PDF file
doc = DocumentFile.from_pdf(pdf_path)

# Load pre-trained model
model = ocr_predictor(pretrained=True)

# Perform OCR
result = model(doc)

# Print recognized text
print(result.render())
