import pdfkit

html_file = 'index.html'
pdf_file = 'index.pdf'
pdfkit.from_file(html_file, pdf_file)
