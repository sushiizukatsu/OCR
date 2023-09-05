import cv2
import fitz
import numpy as np
from PIL import Image
import pyocr

PATH_PDF = 'data/p値の是非を考える.pdf'

# PDFの画像化
pages = fitz.open(PATH_PDF)
pixmap = pages[0].get_pixmap(dpi=400)

img_bytes = np.frombuffer(pixmap.samples_mv, dtype=np.uint8)
img_array = img_bytes.reshape((pixmap.height, pixmap.width, -1))

# 画像の文字認識
tools = pyocr.get_available_tools()
tool = tools[0]
print("Will use tool '%s'" % (tool.get_name()))

tesseract_layout = 6
boxes = tool.image_to_string(
    Image.fromarray(img_array),
    lang='jpn+eng',
    builder=pyocr.builders.WordBoxBuilder(tesseract_layout=tesseract_layout)
)

text_ocr = ''.join([i.content for i in boxes])
print(text_ocr)