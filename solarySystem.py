from flask import json
from classes.planet_class import Planet

def getPlanetData() : 
    with open("solarySystemConsts.json") as f:
        data = json.load(f)
        planets = {}
        for body in data['bodies']:
            if body['isPlanet']:
                planets[body['englishName']] = {
                    'mass': body.get('mass', {}).get('massValue', 0),
                    'radius': body.get('meanRadius', 0),
                    'distance_from_sun': body.get('semimajorAxis', 0),  # in km
                    'gravity': body.get('gravity', 0),
                    'orbitalPeriod': body.get('sideralOrbit', 0), # in days
                }
        return planets
    
def buildPlanets():
    planets = getPlanetData()
    planetsObjects = [
        Planet(name, 
               data["radius"], 
               data["mass"], 
               data["distance_from_sun"], 
               data["gravity"], 
               data["orbitalPeriod"])
        for name, data in planets.items()
    ]
    return planetsObjects
