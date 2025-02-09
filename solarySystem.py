import datetime
import json
from calculations import *
from classes.planet_class import Planet
from astroquery.jplhorizons import Horizons

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
            data["orbitalPeriod"],
            getPlanetAngle(name))
        for name, data in planets.items()
    ]
    return planetsObjects

def getPlanetAngle(planetName):
    """ Récupère l'angle initial de la planète par rapport à l'axe x """
    pos = getPlanetPosition(planetName, datetime.datetime.now(datetime.timezone.utc))
    angleXYZ = math.atan2(pos["z"], math.sqrt(pos["x"]**2 + pos["y"]**2))
    return angleXYZ

def buildPlanet(planetName):
    """ Construit un objet Planet à partir du nom de la planète """
    planets = getPlanetData()
    p = planets[planetName]
    return Planet(p['name'], p['radius'], p['mass'], p['distance_from_sun'], p['gravity'], p['orbitalPeriod'])

def getPlanetIds():
    """Renvoie un dictionnaire contenant les ID des planètes et leurs noms"""
    return {
        "Earth": "399", 
        "Moon": "301",
        "Mars": "499",
        "Jupiter": "599",
        "Venus": "299",
        "Mercury": "199",
        "Neptune": "899",
        "Saturn": "699",
        "Uranus": "799"
    }

def getPlanetPosition(planet_name, date_time):
    """Récupère la position héliocentrique (x, y, z) d'une planète à une date donnée"""
    planet_ids = getPlanetIds()
    planet_id = planet_ids[planet_name]  
    planet_data = getPlanetData()
    jd_now = date_time.timestamp() / 86400 + 2440587.5 
    obj = Horizons(id=planet_id, location='500@0', epochs=[jd_now], id_type='majorbody')
    eph = obj.vectors()

    x = eph['x'][0] * 1.496e+11  
    y = eph['y'][0] * 1.496e+11
    z = eph['z'][0] * 1.496e+11  

    return {"x": x, "y": y, "z": z, "gravity": planet_data[planet_name]["gravity"]} 

def getPlanetsPositions():
    """Renvoie les positions de toutes les planètes du système solaire"""
    date_time = datetime.datetime.now(datetime.timezone.utc)
    planets = getPlanetData()
    positions = {name: getPlanetPosition(name, date_time) for name in planets}
    return positions