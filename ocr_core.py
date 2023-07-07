from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = \
    r'C:\Program Files\Tesseract-OCR\tesseract.exe'


async def ocr_core(file_path: str, writing_style: str) -> str:
    """
    This function will handle the core OCR processing of images.
    """
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image, lang=writing_style)
    return text


if __name__ == '__main__':
    print(ocr_core('img/12_page-0003.jpg'))
