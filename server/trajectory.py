import heapq
import numpy as np
from solarySystem import *

def distance(planetA, planetB):
    """
    Computes the Euclidean distance between two planets in 3D space.

    Returns:
        float: The computed Euclidean distance in meters.
    """
    posA = np.array([planetA["x"], planetA["y"], planetA["z"]])
    posB = np.array([planetB["x"], planetB["y"], planetB["z"]])
    return np.linalg.norm(posA - posB)

def cost_function(planetA, planetB):
    """
    Computes the movement cost between two planets.

    The cost is determined based on both the distance and the gravitational influence 
    of the planets. Higher gravity can be leveraged for slingshot maneuvers, reducing 
    fuel consumption.

    Returns:
        float: A weighted cost value considering distance and gravity effects.
    """
    d = distance(planetA, planetB)
    gravity_effect = (planetA["gravity"] + planetB["gravity"]) / 2  # Average gravity effect
    return d * (1 / gravity_effect)  # Lower cost for planets with higher gravity => Saturn, Venus

def heuristic(planetA, planetB):
    """
    Estimates the remaining distance to the goal using a heuristic.

    The heuristic is the straight-line distance between the current planet and the goal, 
    scaled down to maintain manageable values for our A* algorithm.

    Returns:
        float: The heuristic value, which is the estimated remaining distance in billion meters.
    """
    return distance(planetA, planetB) / 1e9  # Scale down to avoid large numbers in A*

def findOptimalPath(start_planet, goal_planet):
    """
    Finds the optimal trajectory from a starting planet to a destination using A* algorithm.

    The algorithm prioritizes paths that minimize both distance and fuel consumption 
    by considering gravity effects for possible slingshot maneuvers.

    Returns:
        dict: A dictionary containing:
            - "best_route" (list): The optimal sequence of planets to travel through.
            - "total_cost" (float): The computed cost of the optimal path.
        If no path is found, returns a dictionary with an error message.
    """
    planets = getPlanetsPositions()

    goal_pos = planets[goal_planet]  # Our target planet's position

    # Priority queue (min-heap) for our A* search
    open_set = []
    heapq.heappush(open_set, (0, start_planet, [start_planet], 0))  

    # Dictionary to store the best-known cost to reach each planet
    g_score = {planet: float('inf') for planet in planets} # we set a max num at the begining for first comparison
    g_score[start_planet] = 0

    while open_set:
        _, current_planet, path, cost = heapq.heappop(open_set)

        # If we reached the goal, return the computed best route and cost
        if current_planet == goal_planet:
            return {"best_route": path, "Cout total": cost}

        for neighbor in planets:
            if neighbor == current_planet:
                continue
            
            neighbor_pos = planets[neighbor]
            move_cost = cost_function(planets[current_planet], neighbor_pos)

            tentative_g_score = g_score[current_planet] + move_cost

            # If this new path is cheaper than the previously recorded one, we update it
            if tentative_g_score < g_score[neighbor]:
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor_pos, goal_pos)
                heapq.heappush(open_set, (f_score, neighbor, path + [neighbor], tentative_g_score))

    return {"error": "Aucun chemin valide trouvé"}
