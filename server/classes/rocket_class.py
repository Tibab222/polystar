import math
import numpy as np
import datetime
from astroquery.jplhorizons import Horizons

class Rocket:
    def __init__(self, name, speed, departure_planet):
        """Initialise la fusée"""
        self.name = name
        self.speed = np.array([speed, 0])  # (vx, vy)
        self.position = np.array(departure_planet.position_at_time(0))
        self.gas = 100  # Carburant (en %)
        self.time = 0  # Temps total écoulé
        self.steps = []  # Historique des déplacements
        self.steps.append({
            "planet": departure_planet.name,
            "position": self.position,
            "fuel": self.gas,
            "time": self.time
        })
        self.current_planet = departure_planet  # Dernière planète visitée

    def __str__(self):
        return f"{self.name} est à {self.position} avec {self.gas}% de carburant"

    def get_planet_position_at_arrival(self, planet, time_elapsed):
        return np.array(planet.position_at_time(time_elapsed))

    def calculate_slingshot(self, planet):
        G = planet.gravity
        impact_parameter = planet.radius * 1.5 
        v_relative_in = self.speed - planet.averageSpeed  
        v_rel_norm = np.linalg.norm(v_relative_in) 

        delta_theta = 2 * math.atan((G * planet.mass) / (impact_parameter * v_rel_norm ** 2))

        cos_theta = math.cos(delta_theta)
        sin_theta = math.sin(delta_theta)
        rotation_matrix = np.array([[cos_theta, -sin_theta], [sin_theta, cos_theta]])
        v_relative_out = np.dot(rotation_matrix, v_relative_in)

        return v_relative_out + planet.averageSpeed 

    def move_to_planet(self, planet):
        """Déplace la fusée vers la planète cible en ajustant vitesse et carburant"""
        self.gas -= 5

        distance = np.linalg.norm(self.position - planet.position_at_time(self.time))
        time_to_reach = distance / np.linalg.norm(self.speed)  # en secondes
        new_planet_position = self.get_planet_position_at_arrival(planet, time_to_reach)

        new_speed = self.calculate_slingshot(planet)

        fuel_consumption = (distance / 10000) / np.linalg.norm(new_speed) * 0.2

        self.position = new_planet_position
        self.speed = new_speed
        self.gas -= (fuel_consumption - 100) / 100
        self.time += time_to_reach
        self.current_planet = planet

        self.steps.append({
            "planet": planet.name,
            "position": self.position.tolist(),
            "speed": self.speed.tolist(),
            "fuel": self.gas,
            "time": self.time
        })

        return distance, time_to_reach
