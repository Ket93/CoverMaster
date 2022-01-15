from App import app, evaluate
from flask.globals import request

@app.route('/')
def index():
    return "invalid"

@app.route('/submit', methods=['POST'])
def sorting():
    if (request.get_json(force=True)['url']):
        givenUrl = request.get_json(force=True)['url']
        result = evaluate.getResult(str(givenUrl))
        print(result)
        return 'Unreliable' if result else 'Reliable'
