from calculations import average_planet_speed


class Planet:
    def __init__(self, name, radius, mass, distanceFromSun, gravity, orbitalPeriod):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distanceFromSun = distanceFromSun
        self.gravity = gravity
        self.orbitalPeriod = orbitalPeriod
        self.angularSpeed = average_planet_speed(distanceFromSun, orbitalPeriod)
    
    def __str__(self):
        return f"{self.name} est une planète de masse {self.mass} kg et de rayon {self.radius} mètres, située à {self.distanceFromSun} km du Soleil."
    