import flask
from flask_cors import CORS
from utils.number import gen
from utils.picture import gen_img
from utils.alphabet import gen_alphabet
from utils.permute import gen_permute_sets
from utils.dice import gen_dice_sets
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
    # import random
    number = gen("binary")
    rgb = (int(gen("int")), int(gen("int")), int(gen("int")))
    appInfo = {
        "number": number,
        "img": "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
        "pixel": f"rgb{rgb}",
        "alphabet": gen_alphabet(),
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

@app.route('/Picture', methods=['POST'])
def get_colours():
    request_data = request.get_json()
    fig = gen_img()
    return jsonify({"pixel": fig})

@app.route('/Alphabet', methods=['POST'])
def get_alphabet():
    request_data = request.get_json()
    aplphbet = gen_alphabet()
    return jsonify({"Random Alphabet": aplphbet})

@app.route('/Permute', methods=['POST'])
def get_permute():
    request_data = request.get_json()
    sets = request_data['sets']
    ran = request_data['ran']
    return jsonify(gen_permute_sets(sets, ran))

@app.route('/Dice', methods=['POST'])
def get_dice():
    request_data = request.get_json()
    sets = request_data['sets']
    ran = request_data['ran']
    min_num = request_data['min_num']
    max_num = request_data['max_num']
    return jsonify(gen_dice_sets(sets, ran, min_num, max_num))

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
    CORS(app)
        # from waitress import serve
        # serve(app, host="0.0.0.0", port=8080)