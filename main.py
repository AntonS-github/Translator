from googletrans import Translator
import pathlib
import pdfplumber
import os
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen.canvas import Canvas
from gtts import gTTS


def pdf_translator(src_path):
    if pathlib.Path(src_path).is_file and pathlib.Path(src_path).suffix == '.pdf':
        print(f'Source file is {pathlib.Path(src_path).name}')
        print('Loading...')
        with pdfplumber.PDF(open(file=src_path, mode='rb')) as src_pdf:
            pages = [page.extract_text() for page in src_pdf.pages]
        src_text = ''.join(pages)
        print(src_text)
        translator = Translator()
        res_text = translator.translate(src_text)
        print(res_text.text)
        os.chdir('res_path')
        canvas = Canvas('result.pdf', pagesize=LETTER)
        canvas.setPageSize((400, 400))
        canvas.setFont("Times-Roman", 8)
        canvas.drawString(10, 380, res_text.text)
        canvas.save()


def main():
    pdf_translator('C:\\Users\\anvla\\Desktop\\Учёба\\py\\Translator\\src_files\\Test.pdf')


if __name__ == '__main__':
    main()
