import docx
import pandas as pd


def parse_txt_md(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        return [para.strip() for para in f.read().split('\n\n') if para.strip()]


def parse_docx(file_path):
    doc = docx.Document(file_path)
    return [p.text.strip() for p in doc.paragraphs if p.text.strip()]


def parse_excel(file_path):
    xls = pd.ExcelFile(file_path)
    chunks = []
    for sheet_name in xls.sheet_names:
        df = pd.read_excel(xls, sheet_name=sheet_name)
        for _, row in df.iterrows():
            row_text = ' | '.join([str(cell) for cell in row if pd.notna(cell)]).strip()
            if row_text:
                chunks.append(row_text)
    return chunks
