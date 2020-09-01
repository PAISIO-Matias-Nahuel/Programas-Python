import PyPDF2
import os.chdir('ejemplo')
pdffile = open('archivopdf', 'rb')
reader = PyPDF2.PdfFileReader(pdFile)
reader.numPages
reader.getPage(0)
page.extractText()

for pageNum in range(reader.numPages):
    print(reader.getPage(pageNum).extractText()

import PyPDF2
pdfFile = open('ejemplo.pdf','rb')
pdf2File = open('ejemplo2.pdf','rb')

reader1 = PyPDF2.pdfFileReader(pdfFile)
reader2 = PyPDF2.pdfFileReader(pdf2File)

writer = PyPDF2.pdFileWriter()
for pageNum in range(reader1, numpage):
    page = reader2.getPage(pageNum)
    writer.addPage(page)

outputFile = open('ejempll')
writer.write(outputFile)
outputFile.close()
pdf1File.close()
pdf2File.close()
