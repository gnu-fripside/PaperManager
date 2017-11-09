from pdfminer.pdfparser import PDFParser
from pdfminer.pdfparser import PDFDocument
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.layout import *
from pdfminer.converter import PDFPageAggregator
import platform
import sys

class PDF_Manage():
    def __init__(self,fname):
        self.file_name = fname
        self.fp = open(self.file_name,"rb")
        self.parser = PDFParser(self.fp)
        self.doc = PDFDocument()
        self.parser.set_document(self.doc)
        self.doc.set_parser(self.parser)
        self.doc.initialize()
        pass
    def __del__(self):
        self.fp.close()

if __name__ == "__main__":
    doc = PDF_Manage("GAN.pdf")
    print(doc.file_name)

