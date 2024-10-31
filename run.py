import flask
import numpy as np
from pathlib import Path
from flask_cors import CORS
from utils.number import gen
from utils.picture import gen_img
from utils.alphabet import gen_alphabets
from utils.permute import gen_permute_sets
from utils.dice import gen_dice_sets
from flask import render_template, request, jsonify

app = flask.Flask(__name__)

global random_number
global idx

def load_file():
    global random_number, idx
    datas = list(Path("./data/").glob("*.npy"))[0]
    random_number = np.load(str(datas))
    idx = 0

def check_file():
    pass
    # if idx >= 2048:
    #     files = list(Path("./data/").glob("*.npy"))[0]
    #     Path(files).unlink()
    #     load_file()

if __name__ == "__main__":
    load_file()

@app.route('/')
def hello():
    appInfo = {
        "number": 123,
    }
    return render_template('HomePage.html', appInfo=appInfo)

@app.route('/random/')
def random():
    global random_number, idx
    # import random
    number = gen("binary", random_number=random_number, idx=idx)
    rgb, idx = gen_img(random_number=random_number, idx=idx)
    alphabets, idx = gen_alphabets(random_number=random_number, idx=idx)
    appInfo = {
        "number": number,
        "img": "https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png",
        "pixel": f"rgb{rgb}",
        "alphabet": alphabets,
    }
    check_file()
    return render_template('Random_num.html', appInfo=appInfo)

@app.get('/test')
def generate():
    global random_number, idx
    output, idx = gen(random_number=random_number, idx=idx)
    check_file()
    return "Random Number = " + output

@app.route('/pixel')
def pix():
    global random_number, idx
    r, idx = gen("int", random_number=random_number, idx=idx)
    g, idx = gen("int", random_number=random_number, idx=idx)
    b, idx = gen("int", random_number=random_number, idx=idx)
    rgb = (int(r), int(g), int(b))
    check_file()
    return f"rgb{rgb}"

@app.route('/Generate', methods=['POST'])
def get_numbers():
    global random_number, idx
    request_data = request.get_json()
    Type = request_data['Type']
    number, idx = gen(Type, random_number, idx)
    check_file()
    return jsonify({"Random Number": number})

@app.route('/Picture', methods=['POST'])
def get_colours():
    global random_number, idx
    request_data = request.get_json()
    fig, idx = gen_img(random_number=random_number, idx=idx)
    check_file()
    return jsonify({"pixel": fig})

@app.route('/Alphabet', methods=['POST'])
def get_alphabet():
    global random_number, idx
    request_data = request.get_json()
    aplphbet, idx = gen_alphabets(random_number=random_number, idx=idx)
    check_file()
    return jsonify({"Random Alphabet": aplphbet})

@app.route('/Permute', methods=['POST'])
def get_permute():
    global random_number, idx
    request_data = request.get_json()
    sets = request_data['sets']
    ran = request_data['ran']
    out_sets, idx = gen_permute_sets(sets, ran, random_number=random_number, idx=idx)
    check_file()
    return jsonify(out_sets)

@app.route('/Dice', methods=['POST'])
def get_dice():
    global random_number, idx
    request_data = request.get_json()
    sets = request_data['sets']
    ran = request_data['ran']
    min_num = request_data['min_num']
    max_num = request_data['max_num']
    dice_sets, idx = gen_dice_sets(sets, ran, min_num, max_num, random_number=random_number, idx=idx)
    check_file()
    return jsonify(dice_sets)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
    CORS(app)
        # from waitress import serve
        # serve(app, host="0.0.0.0", port=8080)