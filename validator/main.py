from .markdown_parser import validate_markdown
from .pdf_parser import validate_pdf
import os

def main():
    resumes = os.listdir("sample")
    for filename in resumes:
        path = os.path.join("sample", filename)
        if filename.endswith(".md"):
            validate_markdown(path)
        elif filename.endswith(".pdf"):
            validate_pdf(path)

if __name__ == "__main__":
    main()