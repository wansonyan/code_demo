'''
Descripttion: 
version: 
Author: Ryan
Date: 2023-12-15 16:39:46
LastEditors: Ryan
LastEditTime: 2023-12-21 17:41:33
'''
import fitz  # pip install PyMuPDF
def merge_pdfs(pdf1_path, pdf2_path, output_path):
    pdf1 = fitz.open(pdf1_path)
    pdf2 = fitz.open(pdf2_path)

    merged_pdfs = fitz.open()

    for page_num in range(pdf1.page_count):
        page = pdf1[page_num]
        merged_pdfs.insert_pdf(pdf1, from_page=page_num, to_page=page_num, start_at=merged_pdfs.page_count)

    for page_num in range(pdf2.page_count):
        page = pdf1[page_num]
        merged_pdfs.insert_pdf(pdf2, from_page=page_num, to_page=page_num, start_at=merged_pdfs.page_count)

    merged_pdfs.save(output_path)

    pdf1.close()
    pdf2.close()
    merged_pdfs.close()

pdf1_path = 'F:\WorkFile\helmet\color.pdf'
pdf2_path = 'F:\WorkFile\helmet\model_v2.pdf'
output_path = 'F:\WorkFile\helmet\merged.pdf'

merge_pdfs(pdf1_path, pdf2_path, output_path)
  
