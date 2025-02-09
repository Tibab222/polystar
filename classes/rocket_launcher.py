from typing import List

from classes.planet_class import Planet
from classes.rocket_class import Rocket


class RocketLauncher:
    def __init__(self, planets: List[Planet]):
        self.rockets:List[Rocket] = []
        self.planets = planets

    def add_rocket(self, rocket, path):
        self.rockets.append((rocket, path))

    def runAllRockets(self):
        for rocket, path in self.rockets:  # Déstructuration du tuple
            for planet_name in path:  # On itère sur les noms des planètes
                # Trouver la planète correspondante dans la liste des planètes
                planetToGo = next((p for p in self.planets if p.name == planet_name), None)
                
                if planetToGo:  # Vérifier que la planète a été trouvée
                    rocket.moveToPlanet(planetToGo)
                else:
                    print(f"⚠️ Planète {planet_name} introuvable !")


    def find_best_path(self):
        self.runAllRockets()
        # print the rockets steps
        bestTime = 999999999999999999999999
        bestTimeRocket = None
        bestTimePath = None
        bestDistance = 999999999999999999999999
        bestDistanceRocket = None
        bestDistancePath = None
        lowestGasExpense = 999999999999999999999999
        lowestGasExpenseRocket = None
        lowestGasExpensePath = None
        for rocket, path in self.rockets:
            if rocket.time < bestTime:
                bestTime = rocket.time
                bestTimeRocket = rocket
                bestTimePath = path
            if rocket.distance < bestDistance:
                bestDistance = rocket.distance
                bestDistanceRocket = rocket
                bestDistancePath = path
            if rocket.gas < lowestGasExpense:
                lowestGasExpense = rocket.gas
                lowestGasExpenseRocket = rocket
                lowestGasExpensePath = path
        return {
            'bestTime': bestTime,
            'bestTimeRocket': bestTimeRocket,
            'bestTimePath': bestTimePath,
            'bestDistance': bestDistance,
            'bestDistanceRocket': bestDistanceRocket,
            'bestDistancePath': bestDistancePath,
            'lowestGasExpense': lowestGasExpense,
            'lowestGasExpenseRocket': lowestGasExpenseRocket,
            'lowestGasExpensePath': lowestGasExpensePath
        }