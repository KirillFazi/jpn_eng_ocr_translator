import os

from starlette.applications import Starlette
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates
from starlette.responses import RedirectResponse

import uvicorn

from ocr_core import ocr_core
from translator import translator


UPLOAD_FOLDER = 'static/uploads/'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
SAVE_ALL_UPLOADS = False

templates = Jinja2Templates(directory='templates')


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_file(file_path: str, file, is_save_all: bool = False) -> str:
    if is_save_all:
        i = 1
        while os.path.exists(file_path):
            file_path = os.path.join(UPLOAD_FOLDER, f'{i}_{file.filename}')
            i += 1
        with open(file_path, 'wb') as f:
            f.write(file)

    else:
        with open(file_path, 'wb') as f:
            f.write(file)

    return file_path


async def home_page(request):
    return RedirectResponse(url='/upload')


async def upload_page(request):
    if request.method == 'POST':
        form = await request.form()
        # check if there is a file in the request
        if 'file' not in form:
            return templates.TemplateResponse('upload.html', {'request': request, 'msg': 'No file selected'})
        file = form['file']
        # if no file is selected
        if file.filename == '':
            return templates.TemplateResponse('upload.html', {'request': request, 'msg': 'No file selected'})

        if allowed_file(file.filename):
            file_path = save_file(
                os.path.join(UPLOAD_FOLDER, file.filename),
                await file.read(),
                is_save_all=SAVE_ALL_UPLOADS
            )

            extracted_text = await ocr_core(
                file_path=file_path,
                writing_style=form.get('writing-style')
            )

            translated_text = await translator(extracted_text)

            return templates.TemplateResponse('upload.html',
                                              {'request': request, 'msg': 'Successfully processed',
                                               'extracted_text': translated_text,
                                               'img_src': file_path})
        else:
            return templates.TemplateResponse('upload.html',
                                              {'request': request, 'msg': 'Allowed file types are png, jpg, jpeg'})
    elif request.method == 'GET':
        return templates.TemplateResponse('upload.html', {'request': request})


app = Starlette(debug=True, routes=[
    Route('/', home_page),
    Route('/upload', upload_page, methods=['GET', 'POST']),
    Mount('/static', StaticFiles(directory='static'), name='static')
])

if __name__ == '__main__':
    uvicorn.run(app, port=8000)
