from flask import Flask, jsonify
from solarySystem import *

import calculations

app = Flask(__name__)

@app.route('/')
def home():
    solarySystem = buildPlanets()
    for planet in solarySystem:
        print(planet)
        print(planet.position_at_time(20))
    return jsonify({"message": "Bienvenue sur mon serveur Flask !"})

@app.route('/calcul')
def calcul_trajectoire():
    return jsonify({"result": "Simulation de trajectoire en cours"})

@app.route("/planets")
def list_planets():
    """ returns data of planets """
    trajectory = calculatePath("Mercury", "Earth", 7000)
    #return getPlanetData()
    return trajectory

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)