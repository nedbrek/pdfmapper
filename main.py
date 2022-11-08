from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.layout import LTTextBoxHorizontal
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfdevice import PDFDevice

# open a PDF file
document = open('test.pdf', 'rb')

# create a PDF resource manager object that stores shared resources
rsrcmgr = PDFResourceManager()
laparams = LAParams()
# create a PDF device object
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
# create a PDF interpreter object
interpreter = PDFPageInterpreter(rsrcmgr, device)

# process each page contained in the document
for page in PDFPage.get_pages(document):
    interpreter.process_page(page)
    layout = device.get_result()
    for element in layout:
        if isinstance(element, LTTextBoxHorizontal):
            print(element.get_text())

