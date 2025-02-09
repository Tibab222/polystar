from flask import Flask, jsonify, request
from classes.best_path_class import BestPathClass
from solarySystem import *
from trajectory import *

app = Flask(__name__)

@app.route('/')
def home():
    solarySystem = buildPlanets()
    for planet in solarySystem:
        print(planet.position_at_time(20))
    return jsonify({"message": "Bienvenue sur mon serveur Flask !"})

@app.route('/calcul')
def calcul_trajectoire():
    return jsonify({"result": "Simulation de trajectoire en cours"})

@app.route("/planets")
def list_planets():
    """ returns data of planets """
    trajectory = calculatePath("Mercury", "Neptune", 7000)
    #return getPlanetData()
    return trajectory

@app.route("/path/<origin>/<destination>")
def bestPath(origin, destination):
    """ returns the best path """
    bestPath = BestPathClass(buildPlanets(), origin, destination)
    bestPath.createRockets()
    bestOne = bestPath.findBestPath()
    # make a json with the name of planet and the angle
    bestRocket: Rocket = bestOne['bestTimeRocket']
    bestTimePath = []
    for path in bestRocket.steps:
        bestTimePath.append({"targetX": path[0], "targetY": path[1], "time": path[2]})
    return jsonify({"path": bestTimePath})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)