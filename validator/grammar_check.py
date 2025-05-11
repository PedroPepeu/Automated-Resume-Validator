import language_tool_python

tool = language_tool_python.LanguageTool('en-US')

def check_grammar(text, filename):
    matches = tool.check(text)
    report_path = f"reports/{filename.replace('/','_')}.txt"

    with open(report_path, 'w') as report:
        report.write(f"Grammar issues found in {filename}:\n\n")
        for match in matches:
            report.write(f"{match.ruleId}: {match.message}\n")
            report.write(f" Context: {match.context}\n\n")

    print(f"Grammar report saved to {report_path}")