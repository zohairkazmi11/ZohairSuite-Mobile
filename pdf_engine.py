import fitz
from PIL import Image

class PDFEngine:
    def __init__(self, path):
        self.doc = fitz.open(path)
        self.page = 0

    def count(self):
        return len(self.doc)

    def render(self, i):
        p = self.doc.load_page(i)
        pix = p.get_pixmap()
        return Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
