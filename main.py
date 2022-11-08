from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams
from pdfminer.layout import LTFigure
from pdfminer.layout import LTRect
from pdfminer.layout import LTTextBoxHorizontal
from pdfminer.layout import LTTextLineHorizontal
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfdevice import PDFDevice
import sys

# open a PDF file
if len(sys.argv) < 2:
    pdf_name = "test.pdf"
else:
    pdf_name = sys.argv[1]

document = open(pdf_name, 'rb')

# create a PDF resource manager object that stores shared resources
rsrcmgr = PDFResourceManager()
laparams = LAParams()
# create a PDF device object
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
# create a PDF interpreter object
interpreter = PDFPageInterpreter(rsrcmgr, device)

# process each page contained in the document
last_y = -1
line_txt = ""
for page in PDFPage.get_pages(document):
    interpreter.process_page(page)
    layout = device.get_result()
    for element in layout:
        if isinstance(element, LTTextBoxHorizontal):
            print("N1 {}".format(element.get_text()))
        elif isinstance(element, LTFigure):
            pass
        elif isinstance(element, LTRect):
            pass
        elif isinstance(element, LTTextLineHorizontal):
            x0,x1 = element.bbox[0], element.bbox[1]
            y0,y1,txt = element.bbox[2], element.bbox[3], element.get_text().strip('\n')
            #print("N3 {} {} {} {} '{}'".format(x0, x1, y0, y1, txt))
            if last_y == -1:
                line_txt = txt
            elif abs(y1 - last_y) < 1e-6:
                line_txt = line_txt + txt
            else:
                print("N2 {}".format(line_txt))
                line_txt = txt

            last_y = y1
        else:
            print("Ned {}".format(type(element).__name__))

