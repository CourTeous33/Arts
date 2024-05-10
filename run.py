import flask
from flask_cors import CORS
from utils.functions import gen
from flask import render_template, request, jsonify

app = flask.Flask(__name__)

@app.route('/')
def hello():
    appInfo = {
        "number": 123,
    }
    return render_template('HomePage.html', appInfo=appInfo)

@app.route('/random/')
def random():
    import random
    appInfo = {
        "number": random.randint(1, 100),
        "img": "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
    }
    return render_template('Random_num.html', appInfo=appInfo)

@app.get('/test')
def generate():
    output = gen()
    return "Random Number = " + output

@app.route('/Generate', methods=['POST'])
def get_numbers():
    request_data = request.get_json()
    Type = request_data['Type']
    return jsonify({"Random Number": gen(Type)})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
    CORS(app)
        # from waitress import serve
        # serve(app, host="0.0.0.0", port=8080)