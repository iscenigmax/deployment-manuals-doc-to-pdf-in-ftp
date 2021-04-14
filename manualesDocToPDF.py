# pip install docx2pdf

import os
from docx2pdf import convert

# convert("input.docx")
# convert("input.docx", "output.pdf")
# convert(\\)

root = ""

for base, dirs, files in os.walk(root):
	# if os.path.isdir(path):
	convert(base)