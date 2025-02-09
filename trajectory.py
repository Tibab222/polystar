import heapq
import numpy as np
from classes.rocket_class import Rocket
from solarySystem import *

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
    rocket = Rocket("Voyager", initialSpeed, departurePlanet)
    planets.sort(key=lambda x: rocket.distanceFrom(x))
    # for planet in planets:
    #     print(planet.name, rocket.distanceFrom(planet), planet.initial_angle)

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