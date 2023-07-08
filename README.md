# OCR and Translation Web Service

This is a mini-project written in Python that recognizes Japanese text using OCR (Optical Character Recognition) 
and performs its translation into English using another neural network model. 
The project is implemented as a web service using the Starlette framework.

## Features

- Recognize Japanese text in images using OCR (Tesseract).
- Translate the recognized text from Japanese to English using a neural network model provided by 
transformers (Hugging Face). Model name: `Helsinki-NLP/opus-mt-ja-en`.
- User-friendly web interface for uploading images and displaying the results.
- Supports image files with the extensions: `.png`, `.jpg`, and `.jpeg`.

## Prerequisites

- Python 3.6 or above.
- Tesseract (OCR engine) installed on your system.
- Internet connection to access the Hugging Face translation model or a local copy of the model (`Helsinki-NLP/opus-mt-ja-en`).
- The required Python packages are listed in the `requirements.txt` file.

#### OR

- Docker installed on your machine. You can download and install Docker 
from the official Docker website: [https://www.docker.com/get-started](https://www.docker.com/get-started).

----

## Setup and Installation (Local)

1. Clone the repository:
    
```bash
git clone https://github.com/KirillFazi/jpn_eng_ocr_translator.git
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Download and install Tesseract from the [official repository](https://github.com/tesseract-ocr/tesseract).
4. Copy the files from dir `tessdata` in project to the `tessdata` directory in the Tesseract installation directory. 
For Windows: `C:\Program Files\Tesseract-OCR\tessdata`. 
5. Uncomment a line of code (5) in the `ocr_core.py` file to specify the path to the Tesseract installation directory.
If you have installed Tesseract in a different directory, 
you should change the path in the `ocr_core.py` file.

## Usage (Local)

1. Start the web service by running the following command:

```bash
python app.py
```
The service will be accessible at `http://0.0.0.0:8000`.

2. Open your web browser and navigate to `http://0.0.0.0:8000/upload` - it should be done automatically.

3. Upload an image containing Japanese text using the provided form.

4. The service will process the image, extract the text using OCR, and translate it into English using the neural network model.

5. The translated text and the processed image will be displayed on the web page.

------

## Setup and Installation (Docker)

1. Clone the repository:
    
```bash
git clone https://github.com/KirillFazi/jpn_eng_ocr_translator.git
```

2. Build the Docker image:

```bash
docker build -t ocr_translator .
```

## Usage (Docker)

1. Run the Docker container:

```bash
docker run -d --name ocr_translator -p 8000:8000 ocr_translator
```

2. Open your web browser and navigate to `http://0.0.0.0:8000/upload` - it should be done automatically.

3. Upload an image containing Japanese text using the provided form.

4. The service will process the image, extract the text using OCR, and translate it into English using the neural network model.

5. The translated text and the processed image will be displayed on the web page.

## Project Structure

- `app.py`: The main script that runs the Starlette web service.
- `ocr_core.py`: Module containing the OCR functionality using Tesseract.
- `translator.py`: Module containing the translation functionality using the Hugging Face model.
- `static/`: Directory for storing static files (e.g., uploaded images).
- `templates/`: Directory containing HTML templates for the web pages.

## Contributing

Contributions to this project are welcome. If you find any issues or 
have suggestions for improvements, please open an issue or submit a pull request on the GitHub repository.

---------

---------

# OCR и веб-сервис перевода

Это мини-проект, написанный на Python, который распознает японский текст с помощью OCR (оптического распознавания символов) 
и выполняет его перевод на английский язык с помощью другой нейросетевой модели. 
Проект реализован в виде веб-сервиса с использованием фреймворка Starlette.

## Функции

- Распознавание японского текста на изображениях с помощью OCR (Tesseract).
- Перевод распознанного текста с японского на английский с помощью нейросетевой модели, предоставленной 
transformers (Hugging Face). Имя модели: `Helsinki-NLP/opus-mt-ja-en`.
- Удобный веб-интерфейс для загрузки изображений и отображения результатов.
- Поддерживаются файлы изображений с расширениями: `.png`, `.jpg` и `.jpeg`.

## Необходимые условия

- Python 3.6 или выше.
- Tesseract (движок OCR), установленный в вашей системе.
- Интернет-соединение для доступа к модели перевода Hugging Face или локальная копия модели (`Helsinki-NLP/opus-mt-ja-en`).
- Необходимые пакеты Python перечислены в файле `requirements.txt`.

#### ИЛИ

- На вашей машине установлен Docker. Вы можете загрузить и установить 
Docker с официального сайта Docker: [https://www.docker.com/get-started](https://www.docker.com/get-started).

----

## Настройка и установка (локально)

1. Клонируйте репозиторий:
    
```bash
git clone https://github.com/KirillFazi/jpn_eng_ocr_translator.git
```

2. Установите необходимые пакеты Python:

```bash
pip install -r requirements.txt
```

3. Скачайте и установите Tesseract из [официального репозитория](https://github.com/tesseract-ocr/tesseract).
4. Скопируйте файлы из dir `tessdata` в проекте в директорию `tessdata` в каталоге установки Tesseract. 
Для Windows: `C:\Program Files\Tesseract-OCR\tessdata`. 
5. Откомментируйте строку кода (5) в файле `ocr_core.py`, чтобы указать путь к директории установки Tesseract.
Если вы установили Tesseract в другой каталог, 
вам следует изменить путь в файле `ocr_core.py`.

## Использование (локальное)

1. Запустите веб-сервис, выполнив следующую команду:

```bash
python app.py
```
Служба будет доступна по адресу `http://0.0.0.0:8000`.

2. Откройте веб-браузер и перейдите по адресу `http://0.0.0.0:8000/upload` - это должно произойти автоматически.

3. Загрузите изображение, содержащее японский текст, используя предоставленную форму.

4. Сервис обработает изображение, извлечет текст с помощью OCR и переведет его на английский язык с помощью нейросетевой модели.

5. Переведенный текст и обработанное изображение будут отображены на веб-странице.

------

## Настройка и установка (Docker)

1. Клонируйте репозиторий:
    
```bash
git clone https://github.com/KirillFazi/jpn_eng_ocr_translator.git
```

2. Соберите образ Docker:

```bash
docker build -t ocr_translator .
```

## Использование (Docker)

1. Запустите контейнер Docker:

```bash
docker run -d --name ocr_translator -p 8000:8000 ocr_translator
```

2. Откройте веб-браузер и перейдите по адресу `http://0.0.0.0:8000/upload` - это должно произойти автоматически.

3. Загрузите изображение, содержащее японский текст, используя предоставленную форму.

4. Сервис обработает изображение, извлечет текст с помощью OCR и переведет его на английский язык с помощью нейросетевой модели.

5. Переведенный текст и обработанное изображение будут отображены на веб-странице.

## Структура проекта

- `app.py`: Основной скрипт, запускающий веб-сервис Starlette.
- `ocr_core.py`: Модуль, содержащий функциональность OCR с использованием Tesseract.
- `translator.py`: Модуль, содержащий функциональность перевода с использованием модели Hugging Face.
- `static/`: Каталог для хранения статических файлов (например, загруженных изображений).
- `templates/`: Каталог, содержащий HTML-шаблоны для веб-страниц.

## Вклад

Вклад в этот проект приветствуется. Если вы обнаружили какие-либо проблемы или 
предложения по улучшению, пожалуйста, откройте проблему или отправьте запрос на исправление на репозитории GitHub.

