from transformers import MarianMTModel, MarianTokenizer
import torch

DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
MODEL_NAME = 'Helsinki-NLP/opus-mt-ja-en'


async def translator(extracted_text: str) -> str:
    """
    Translate the extracted text from Japanese to English
    :param extracted_text: extracted text from the image using OCR
    :return: translated English text
    """
    model = MarianMTModel.from_pretrained(MODEL_NAME)
    tokenizer = MarianTokenizer.from_pretrained(MODEL_NAME)

    segmented_text = (
        seg
        .replace('\n', '')
        .replace(' ', '')
        for seg in extracted_text.split('\n\n')
    )

    translated_segments = []
    for segment in segmented_text:
        inputs = tokenizer.encode(segment, return_tensors="pt")

        translated = model.generate(
            inputs,
            max_length=512,
            num_beams=4,
            no_repeat_ngram_size=3
        )

        translated_text = tokenizer.decode(
            translated[0],
            skip_special_tokens=True
        )

        translated_segments.append(f'{translated_text}\n')

    return ''.join(translated_segments)


if __name__ == '__main__':
    text = """日本語のテキストを翻訳することができます。"""
    print(translator(text))
