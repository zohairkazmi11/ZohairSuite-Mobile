import fitz
from PIL import Image
import io

class PDFEngine:
    def __init__(self, path):
        self.doc = fitz.open(path)
        self.page_index = 0

    def page_count(self):
        return len(self.doc)

    def render_page(self, index, zoom=2):
        page = self.doc.load_page(index)
        mat = fitz.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix=mat)

        img_bytes = pix.tobytes("png")
        return img_bytes

    def next_page(self):
        if self.page_index < len(self.doc) - 1:
            self.page_index += 1

    def prev_page(self):
        if self.page_index > 0:
            self.page_index -= 1
