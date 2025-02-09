from flask import Flask, jsonify
from classes.rocket_class import Rocket
from solarySystem import *
from trajectory import *
from classes.planet_class import *

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Bienvenue sur mon serveur Flask !"})

@app.route('/calcul/<origin>/<destination>')
def calcul_trajectoire(origin, destination):
    planets = buildPlanets()
    for planet in planets:
        if planet.name == origin:
            origin_planet = planet
            break
    rocket = Rocket("Fusée", 7900, origin_planet)
    optPath = findOptimalPath(origin, destination)
    route = optPath["best_route"]
    for planet in route:
        for p in planets:
            if p.name == planet:
                planet = p
                break
        rocket.moveToPlanet(planet)
        print(rocket)
        steps = rocket.steps
        returnSteps = []
        for step in steps:
            returnSteps.append({"angle": math.atan2(step[0], step[1]), "planet": step[2]})
    return jsonify({"steps": returnSteps})

@app.route("/planets")
def list_planets():
    """ returns data of planets """ 
    return jsonify(getPlanetsPositions())

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)