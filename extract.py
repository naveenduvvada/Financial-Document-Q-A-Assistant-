import pandas as pd
import pdfplumber

def process_file(uploaded_file):
    name = uploaded_file.name.lower()
    if name.endswith('.pdf'):
        return process_pdf(uploaded_file)
    else:
        return process_excel(uploaded_file)

def process_pdf(uploaded_file):
    text = ''
    tables = []
    with pdfplumber.open(uploaded_file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ''
            for table in page.extract_tables():
                if table:
                    df = pd.DataFrame(table[1:], columns=table[0])
                    tables.append(df)
    return {"text_preview": text[:1000], "tables_found": len(tables)}

def process_excel(uploaded_file):
    xls = pd.ExcelFile(uploaded_file)
    sheets = {s: xls.parse(s).head().to_dict() for s in xls.sheet_names}
    return {"sheets": list(sheets.keys()), "first_sheet_preview": sheets[xls.sheet_names[0]]}
