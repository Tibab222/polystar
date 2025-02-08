import json
import numpy as np
import heapq  

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

def slingshot_velocity(v_in, planet):
    """ Calcule la vitesse après un slingshot gravitationnel """
    v_planet = planet['orbital_speed'] 
    M = planet['mass']
    r = planet['distance_from_sun']

    delta_v = np.sqrt(v_in**2 + 2 * G * M / r)  
    return delta_v + v_planet  # Ajoute la vitesse de la planète elle-même

def calculatePath(departure, destination, initialSpeed):
    """ Trouve la meilleure trajectoire en minimisant la consommation de carburant """
    planets = getPlanetData()

    if departure not in planets or destination not in planets:
        return {"error": "Planète inconnue"}

    queue = []
    heapq.heappush(queue, (0, departure, initialSpeed, [departure]))  # (cost, current_planet, speed, path)
    
    visited = {}

    while queue:
        cost, current, speed, path = heapq.heappop(queue)

        if current == destination:
            return {"best_route": path, "fuel_efficiency": cost}

        if current in visited and visited[current] <= cost:
            continue 

        visited[current] = cost

        for next_planet in planets.keys():
            if next_planet in path:  
                continue

            new_speed = slingshot_velocity(speed, planets[next_planet])
            new_cost = cost + (1 / new_speed) 

            heapq.heappush(queue, (new_cost, next_planet, new_speed, path + [next_planet]))

    return {"error": "Aucune trajectoire trouvée"}

