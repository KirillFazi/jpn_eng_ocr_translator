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

TEMPLATES = Jinja2Templates(directory='templates')


def allowed_file(filename: str) -> bool:
    """
    Check if the file extension is allowed
    :param filename: filename for checking
    :return: True if the file extension is allowed, False otherwise
    """
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def save_file(file_path: str, file, is_save_all: bool = False) -> str:
    """
    Save the file to the specified path and return the path
    :param file_path:
    :param file: file to save. In this case, it is a byte string
    :param is_save_all: if True, save all files with the same name
    and add prefix for all duplicates. If False, replace duplicate file names
    :return: path to the saved file. If is_save_all is False, it is the same as file_path
    """
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
    """
    Redirect to the upload page
    :param request: incoming request. In this case, it's not used
    :return: RedirectResponse to the upload page
    """
    return RedirectResponse(url='/upload')


async def upload_page(request):
    """
    Upload page. POST method is used for uploading files and GET method is used for rendering the page
    :param request: incoming request. In this case we use it for getting the form data.
    :return: TEMPLATES.TemplateResponse with the upload page
    """
    if request.method == 'POST':
        form = await request.form()
        # check if there is a file in the request
        if 'file' not in form:
            return TEMPLATES.TemplateResponse('upload.html', {'request': request, 'msg': 'No file selected'})
        file = form['file']
        # if no file is selected
        if file.filename == '':
            return TEMPLATES.TemplateResponse('upload.html', {'request': request, 'msg': 'No file selected'})

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

            return TEMPLATES.TemplateResponse('upload.html',
                                              {'request': request, 'msg': 'Successfully processed',
                                               'extracted_text': translated_text,
                                               'img_src': file_path})
        else:
            return TEMPLATES.TemplateResponse('upload.html',
                                              {'request': request, 'msg': 'Allowed file types are png, jpg, jpeg'})
    elif request.method == 'GET':
        return TEMPLATES.TemplateResponse('upload.html', {'request': request})


if __name__ == '__main__':
    app = Starlette(debug=True, routes=[
        Route('/', home_page),
        Route('/upload', upload_page, methods=['GET', 'POST']),
        Mount('/static', StaticFiles(directory='static'), name='static')
    ])

    uvicorn.run(app, host='0.0.0.0', port=8000)
