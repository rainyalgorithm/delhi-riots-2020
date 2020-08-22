#!/usr/bin/env python
try:
    import fitz
except ImportError as e:
    import subprocess
    subprocess.call("pip install PyMuPDF".split())
    print('Try pip install PyMuPDF')
    raise
import sys
filename = sys.argv[1]
outfilename = filename.replace('.pdf', '.anon.pdf')
doc = fitz.open(filename)
for page in doc:
    for annot in page.annots():
        info = annot.info
        info['title'] = ''
        annot.setInfo(info)
        annot.update()

doc.save(outfilename)

