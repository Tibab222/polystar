from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Bienvenue sur mon serveur Flask !"})

@app.route('/calcul')
def calcul_trajectoire():
    return jsonify({"result": "Simulation de trajectoire en cours"})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
