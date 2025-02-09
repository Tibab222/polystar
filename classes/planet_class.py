import random
from calculations import average_planet_speed
import math

class Planet:
    def __init__(self, name, radius, mass, distanceFromSun, gravity, orbitalPeriod):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distanceFromSun = distanceFromSun
        self.gravity = gravity
        self.orbitalPeriod = orbitalPeriod
        self.angular_velocity = (2 * math.pi) / orbitalPeriod
        self.initial_angle = random.uniform(0, 2*math.pi)
        self.averageSpeed = average_planet_speed(distanceFromSun, orbitalPeriod)
    
    def __str__(self):
        return f"{self.name} est une planète de masse {self.mass} kg et de rayon {self.radius} mètres, située à {self.distanceFromSun} km du Soleil."
    
    def position_at_time(self, time):
        """Retourne la position (x, y) de la planète à un instant donné"""
        angle = self.initial_angle + self.angular_velocity * time
        x = self.distanceFromSun * math.cos(angle)
        y = self.distanceFromSun * math.sin(angle)
        return x, y
    