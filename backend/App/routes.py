from asyncore import write
from App import app, evaluate
from flask.globals import request


@app.route('/')
def index():
    return "invalid"


@app.route('/submit', methods=['POST'])
def sorting():
    if (request.get_json(force=True)):
        givenUrl = request.get_json(force=True)
        print(givenUrl)

        evaluate.writeDoc(givenUrl)

        return "recieved data"
    return "did not recieve data"
