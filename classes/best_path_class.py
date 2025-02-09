from typing import List
from classes.graph import Graph
from classes.planet_class import Planet
from classes.rocket_launcher import RocketLauncher
from classes.rocket_class import Rocket


class BestPathClass:
    def __init__(self, planets: List[Planet], origin: str, destination: str):
        self.planets = planets
        self.origin = origin
        self.destination = destination
        self.rocketLauncher = RocketLauncher(planets)
    
    def createRockets(self):
        """Retourne toutes les combinaisons possibles de planètes"""
        graph = Graph()
        allPaths = graph.find_all_paths(self.origin, self.destination)
# find the planet in the list of planets
        initPlanet = [planet for planet in self.planets if planet.name == self.origin][0]
        destPlanet = [planet for planet in self.planets if planet.name == self.destination][0]
        for path in allPaths:
            rocket = Rocket("Voyager", 7900, initPlanet)
            self.rocketLauncher.add_rocket(rocket, path)
        return self.rocketLauncher

    def findBestPath(self):
        """Retourne la trajectoire la plus efficace"""
        self.createRockets()
        bestPath = self.rocketLauncher.find_best_path()
        return bestPath