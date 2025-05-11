import markdown
import re
from validator.grammar_check import check_grammar

def validate_markdown(path):
    with open(path, 'r') as file:
        content = file.read()

    required_sections = ["skills", "education", "experience"]
    missing = [s for s in required_sections if s.lower() not in content.lower()]

    print(f"Validating {path}")
    if missing:
        print(f"Missing sections: {', '.join(missing)}")
    else:
        print("All required sections found.")

    check_grammar(content, path)