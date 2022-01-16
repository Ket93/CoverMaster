from asyncore import write
from random import Random
from App import app, evaluate
from flask.globals import request
from flask import send_from_directory, abort
import os


app.config['DOWNLOAD_FILE'] = os.path.abspath('./').replace("\\", "/")


@app.route('/')
def index():
    return "Invalid"


@app.route('/download')
def download_file():
    try:
        return send_from_directory(app.config['DOWNLOAD_FILE'], path="test-output.docx",
                                   as_attachment=True)
    except TypeError:
        return send_from_directory(app.config['DOWNLOAD_FILE'],
                                   filename="test-output.docx", as_attachment=True)
    except FileNotFoundError:
        abort(404)

@app.route('/download/<id>')
def download_file_id():
    try:
        return send_from_directory(app.config['DOWNLOAD_FILE'], path=f"{id}.docx",
                                   as_attachment=True)
    except TypeError:
        return send_from_directory(app.config['DOWNLOAD_FILE'],
                                   filename=f"{id}.docx", as_attachment=True)
    except FileNotFoundError:
        abort(404)

@app.route('/submit', methods=['POST'])
def sorting():
    if (request.get_json(force=True)):
        givenUrl = request.get_json(force=True)
        print(givenUrl)
        randname = f'{Random.randrange(1111, 8888)}'

        evaluate.writeDoc(givenUrl)

        return randname
    return "did not recieve data"
