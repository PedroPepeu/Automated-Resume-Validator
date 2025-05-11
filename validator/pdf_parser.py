from pdfminer.high_level import extract_text
from validator.grammar_check import check_grammar

def validate_pdf(path):
    text = extract_text(path)
    if not text.strip():
        print(f"{path} appears to be empty or enreadable.")
        return
    
    print(f"Extracted text from {path}")
    check_grammar(text, path)