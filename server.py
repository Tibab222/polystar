from flask import Flask, jsonify
from classes.rocket_class import Rocket
from solarySystem import *
from trajectory import *
from classes.planet_class import *
import math

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"message": "Bienvenue sur mon serveur Flask !"})

@app.route('/calcul/<origin>/<destination>')
def calcul_trajectoire(origin, destination):
    planets = buildPlanets()

    origin_planet = next(p for p in planets if p.name == origin)

    rocket = Rocket("Fusée", 7900, origin_planet)
    defaultRocket = Rocket("Fusée", 7900, origin_planet)  # Clone pour comparaison

    optPath = findOptimalPath(origin, destination)
    route = optPath["best_route"]

    for planet_name in route:
        planet = next(p for p in planets if p.name == planet_name)
        rocket.move_to_planet(planet)

    steps = []
    for step in rocket.steps:
        steps.append({
            "planet": step["planet"],
            "position": math.atan2(step["position"][1], step["position"][0]),
            "speed": step["speed"],
            "fuel": step["fuel"],
            "time": step["time"]
        })

    defaultRocket.move_to_planet(next(p for p in planets if p.name == destination))

    return jsonify({
        "optimalPath": optPath,
        "steps": steps,
        "defaultTime": defaultRocket.time,
        "defaultFuelConsumption": defaultRocket.gas
    })


@app.route("/planets")
def list_planets():
    """ returns data of planets """ 
    return jsonify(getPlanetsPositions())


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)