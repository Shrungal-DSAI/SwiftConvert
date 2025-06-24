from app.utils.ocr_with_layoutparser import convert_pdf_to_docx_with_ocr

@router.post("/pdf-to-word-ocr")
async def pdf_to_word_ocr(file: UploadFile = File(...)):
    contents = await file.read()
    input_pdf_path = f"temp/{file.filename}"
    output_docx_path = f"output/{file.filename.replace('.pdf', '.docx')}"

    with open(input_pdf_path, "wb") as f:
        f.write(contents)

    convert_pdf_to_docx_with_ocr(input_pdf_path, output_docx_path)

    return FileResponse(output_docx_path, media_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document', filename=os.path.basename(output_docx_path))
