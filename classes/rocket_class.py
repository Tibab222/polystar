import math

import numpy as np

from classes.planet_class import Planet

class Rocket:
    def __init__(self, name, speed, departure_planet: Planet):
        self.name = name
        self.speed = speed # vitesse actuelle en m/s
        self.distance = 0 # distance parcourue
        self.time = 0 # temps de vol effectué en secondes
        pos = departure_planet.position_at_time(0)
        self.position = (pos[0], pos[1], 0, departure_planet.name) # position actuelle (x, y)
        self.last_planet = departure_planet
        self.steps = [] # historique des positions
        self.steps.append(self.position)
        self.gas = 100 # carburant en %
        self.acceleration = 0
        self.direction = 0 # angle de la direction de la fusée
        # print('Rocket created at', self.position)
    
    def __str__(self):
        return f"{self.name} vole à {self.speed} m/s"
    
    def moveToPosition(self, x, y, speed):
        """"
        Déplace la fusée à la position (x, y) à la vitesse speed.
        Change la position de la fusée et met à jour les attributs
        """
        # Calcul de la distance à parcourir
        distance = math.sqrt((x - self.position[0])**2 + (y - self.position[1])**2)
        # Calcul du temps de vol
        # normalise the speed vector
        speedNorme = np.linalg.norm(speed)
        if speedNorme == 0:
            time = 0
        else:
            time = distance / speedNorme
        # Mise à jour des attributs
        self.distance += distance
        self.time += time
        self.speed = speed
        self.position = (x, y, self.time, self.last_planet.name)
        self.direction = math.atan2(y - self.position[1], x - self.position[0])
        self.steps.append(self.position)
        self.gas -= 10/(1+speedNorme)
        return distance, time
    
    def moveToPlanet(self, planet: Planet):
        """Déplace la fusée à la position de la planète"""
        x, y = planet.position_at_time(self.time_to_orbit(planet))
        distance, time = self.moveToPosition(x, y, self.speed)
        new_speed = self.calculateFlyby(planet)
        self.speed = new_speed
        self.last_planet = planet
        return distance, time
    
    def calculateFlyby(self, planet: Planet):
        """Calcule la nouvelle vitesse pour un slingshot gravitationnel"""
        G = planet.gravity
        impact_parameter = planet.radius * 1.5  # Paramètre d'impact arbitraire
        v_relative_in = self.speed - planet.averageSpeed  # Vitesse relative avant l'approche
        v_rel_norm = np.linalg.norm(v_relative_in)  # Norme de la vitesse relative

        # Calcul de l'angle de déviation
        delta_theta = 2 * math.atan((G * planet.mass) / (impact_parameter * v_rel_norm ** 2))

        # Rotation du vecteur de vitesse relative
        cos_theta = math.cos(delta_theta)
        sin_theta = math.sin(delta_theta)
        rotation_matrix = np.array([[cos_theta, -sin_theta], [sin_theta, cos_theta]])
        v_relative_out = np.dot(rotation_matrix, v_relative_in)

        # Nouvelle vitesse de la fusée
        return v_relative_out + planet.averageSpeed
    
    def time_to_orbit(self, planet: Planet):
        """Calcule le temps nécessaire pour atteindre l'orbite de la planète"""
        d_planet = planet.distanceFromSun - math.sqrt(self.position[0]**2 + self.position[1]**2)

        if self.acceleration == 0:
            # speedNorme is the norm of the speed vector
            speedNorme = np.linalg.norm(self.speed)
            speedNotZero = speedNorme if speedNorme != 0 else 1
            t_arrival = d_planet / speedNotZero
        else:
            t_arrival = (-self.speed + math.sqrt(self.speed**2 + 2 * self.acceleration * d_planet)) / self.acceleration

        return t_arrival
    
    def position_at_time(self, time):
        """Retourne la position (x, y) de la fusée à un instant donné"""
        x = self.position[0] + self.speed * time + 0.5 * self.acceleration * math.cos(self.direction) * time**2
        y = self.position[1] + self.speed * time + 0.5 * self.acceleration * math.sin(self.direction) * time**2
        return x, y
    
    def position_at_planet(self, planet: Planet):
        """Retourne la position (x, y) de la fusée à l'arrivée à la planète"""
        t_arrival = self.time_to_orbit(planet)
        return self.position_at_time(t_arrival)
    
    def distanceFrom(self, planet: Planet):
        """Retourne la distance entre la fusée et une planète"""
        x, y = self.position_at_planet(planet)
        return math.sqrt(x**2 + y**2)