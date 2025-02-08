import json
import numpy as np
import heapq  
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


def slingshot_velocity(v_in, planet: Planet):
    """ Calcule la vitesse après un slingshot gravitationnel """
    v_planet = planet.averageSpeed
    M = planet.mass
    r = planet.distanceFromSun

    delta_v = np.sqrt(v_in**2 + 2 * G * M / r)  
    return delta_v + v_planet  # Ajoute la vitesse de la planète elle-même

def calculatePath(departure, destination, initialSpeed):
    """ Trouve la meilleure trajectoire en minimisant la consommation de carburant """
    departurePlanet = buildPlanet(departure)
    destinationPlanet = buildPlanet(destination)
    planets = buildPlanets()

    queue = []
    heapq.heappush(queue, (0, departurePlanet.name, initialSpeed, [departurePlanet.name]))  # (cost, current_planet_name, speed, path)
    
    visited = {}

    while queue:
        cost, current_name, speed, path = heapq.heappop(queue)

        if current_name == destinationPlanet.name:
            return {"best_route": path, "fuel_efficiency": cost}

        if current_name in visited and visited[current_name] <= cost:
            continue 

        visited[current_name] = cost

        for nextPlanet in planets:
            if nextPlanet.name in path:  # Évite les boucles
                continue

            new_speed = slingshot_velocity(speed, nextPlanet)
            new_cost = cost + (100 / new_speed)  # Facteur pour augmenter l'impact du coût

            heapq.heappush(queue, (new_cost, nextPlanet.name, new_speed, path + [nextPlanet.name]))

    return {"error": "Aucune trajectoire trouvée"}