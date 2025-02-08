import math

from classes.planet_class import Planet

class Rocket:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.distance = 0 # distance parcourue
        self.time = 0 # temps de vol effectué en secondes
        self.speed = 0 # vitesse actuelle en m/s
        self.position = (0, 0) # position actuelle (x, y)
        self.steps = [] # historique des positions
        self.gas = 100 # carburant en %
        self.acceleration = 0
    
    def __str__(self):
        return f"{self.name} vole à {self.speed} m/s"
    
    def moveToPosition(self, x, y, speed):
        """"
        Déplace la fusée à la position (x, y) à la vitesse speed.
        """
        # Calcul de la distance à parcourir
        distance = math.sqrt((x - self.position[0])**2 + (y - self.position[1])**2)
        # Calcul du temps de vol
        time = distance / speed
        # Mise à jour des attributs
        self.distance += distance
        self.time += time
        self.speed = speed
        self.position = (x, y)
        self.steps.append(self.position)
        return distance, time
    
    def time_to_orbit(self, planet: Planet):
        """Calcule le temps nécessaire pour atteindre l'orbite de la planète"""
        d_planet = planet.distanceFromSun - math.sqrt(self.position[0]**2 + self.position[1]**2)

        if self.acceleration == 0:
            t_arrival = d_planet / self.speed
        else:
            t_arrival = (-self.speed + math.sqrt(self.speed**2 + 2 * self.acceleration * d_planet)) / self.acceleration

        return t_arrival
    
    def position_at_time(self, time):
        """Retourne la position (x, y) de la fusée à un instant donné"""
        x = self.x + self.vx * time + 0.5 * self.acceleration * math.cos(self.angle) * time**2
        y = self.y + self.vy * time + 0.5 * self.acceleration * math.sin(self.angle) * time**2
        return x, y
    
    def position_at_planet(self, planet: Planet):
        """Retourne la position (x, y) de la fusée à l'arrivée à la planète"""
        t_arrival = self.time_to_orbit(planet)
        return self.position_at_time(t_arrival)