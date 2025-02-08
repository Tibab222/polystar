import json
from calculations import *
from classes.planet_class import *
G = 6.67430e-11 

def getPlanetData():
    """ Récupère et trie les planètes par distance au Soleil """
    with open("solarySystemConsts.json") as f:
        data = json.load(f)
        planets = []
        for body in data['bodies']:
            if body['isPlanet']:
                planets.append({
                    'name': body['englishName'],
                    'mass': body.get('mass', {}).get('massValue', 0) * 1e24,  # en kg
                    'radius': body.get('meanRadius', 0),
                    'distance_from_sun': body.get('semimajorAxis', 0) * 1e3,  # en mètres
                    'gravity': body.get('gravity', 0),
                    'orbitalPeriod': body.get('sideralOrbit', 0),  # en jours
                })
        planets.sort(key=lambda x: x['distance_from_sun']) # we sort the planets 
        return {p['name']: p for p in planets}
    
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

def buildPlanet(planetName):
    """ Construit un objet Planet à partir du nom de la planète """
    planets = getPlanetData()
    p = planets[planetName]
    return Planet(p['name'], p['radius'], p['mass'], p['distance_from_sun'], p['gravity'], p['orbitalPeriod'])