from PIL import Image                                                                           
from pdf2image import convert_from_path
import os
import sys
import pytesseract as pyr 

file_name = 'text.pdf'
pdf_pages = convert_from_path(file_name, 2)
counter = 1

for i in range(len(images)):
    images[i].save('page'+ str(i) +'.jpg', 'JPEG')