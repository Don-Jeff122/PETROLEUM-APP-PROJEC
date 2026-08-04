import PyPDF2

reader = PyPDF2.PdfReader('C:/Documents/PENG258-PROJECT-2026.pdf')
text = ''
for page in reader.pages:
    text += (page.extract_text() or '') + '\n'

# print key sections
print("=" * 60)
print("PROJECT DELIVERABLES SECTION:")
print("=" * 60)
lines = text.split('\n')
for i, line in enumerate(lines):
    if 'deliverable' in line.lower() or 'assessment' in line.lower():
        for j in range(max(0,i-1), min(len(lines), i+10)):
            print(lines[j])
        print('...')
