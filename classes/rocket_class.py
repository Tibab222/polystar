import math

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