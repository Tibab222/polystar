import heapq
import numpy as np
from solarySystem import *

def distance(planetA, planetB):
    posA = np.array([planetA["x"], planetA["y"], planetA["z"]])
    posB = np.array([planetB["x"], planetB["y"], planetB["z"]])
    return np.linalg.norm(posA - posB)

def cost_function(planetA, planetB):
    """Here we set the cost depending on distance and gravity"""
    d = distance(planetA, planetB)
    gravity_effect = (planetA["gravity"] + planetB["gravity"]) / 2  
    return d * (1 / gravity_effect)

def heuristic(planetA, planetB):
    return distance(planetA, planetB) / 1e9

def findOptimalPath(start_planet, goal_planet):
    planets = getPlanetsPositions()

    if start_planet not in planets or goal_planet not in planets:
        return {"error": "Planète non trouvée"}

    goal_pos = planets[goal_planet]

    open_set = []
    heapq.heappush(open_set, (0, start_planet, [start_planet], 0))  

    g_score = {planet: float('inf') for planet in planets}
    g_score[start_planet] = 0

    while open_set:
        _, current_planet, path, cost = heapq.heappop(open_set)

        if current_planet == goal_planet:
            return {"best_route": path, "total_cost": cost}

        for neighbor in planets:
            if neighbor == current_planet:
                continue
            
            neighbor_pos = planets[neighbor]
            move_cost = cost_function(planets[current_planet], neighbor_pos)

            tentative_g_score = g_score[current_planet] + move_cost

            if tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor_pos, goal_pos)
                heapq.heappush(open_set, (f_score, neighbor, path + [neighbor], tentative_g_score))

    return {"error": "Aucun chemin trouvé"}