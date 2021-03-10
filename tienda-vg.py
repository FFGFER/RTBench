from flask import Flask, jsonify
import sys, os.path
sys.path.append("src/")
import videojuegos

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/status')
def status():
    return jsonify(status="Ok")

@app.route('/')
def index():
    return jsonify(status="Ok")

@app.route('/obtenervg/<idvg>')
def obtenervg(idvg):
    vg = videojuegos.Videojuegos()
    idvg = int(idvg)
    return jsonify(Videojuego=vg.getVideojuego(idvg))

@app.route('/videojuegos')
def vgs():
    vg = videojuegos.Videojuegos()
    return jsonify(Videojuegos=vg.getVideojuegos())

@app.route('/addvg/<nombrevg>')
def addvg(nombrevg):
    vg = videojuegos.Videojuegos()
    return jsonify(Return=vg.aniadeVideojuego(nombrevg))

@app.route('/findvg/<nombrevg>')
def findvg(nombrevg):
    vg = videojuegos.Videojuegos()
    print(type(vg))
    return jsonify(Encontrado=vg.encuentraVideojuego(nombrevg))

@app.route('/deletevg/<nombrevg>')
def deletevg(nombrevg):
    vg = videojuegos.Videojuegos()
    return jsonify(Return=vg.borraVideojuego(nombrevg))



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
