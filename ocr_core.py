from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


async def ocr_core(file_path: str, writing_style: str) -> str:
    """
    Extract text from the image using OCR for Japanese
    :param file_path: path to the image. In this case, we get files from the upload folder(static/uploads)
    :param writing_style: writing style of the text. Can be either 'jpn'(horizontal) or 'jp_vert'(vertical)
    :return: extracted Japanese text
    """
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image, lang=writing_style)
    return text


if __name__ == '__main__':
    print(ocr_core('img/12_page-0003.jpg', 'jpn_vert'))
