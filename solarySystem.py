from flask import json

def getPlanetData() : 
    with open("solarySystemConsts.json") as f:
        data = json.load(f)
        planets = {}
        for body in data['bodies']:
            if body['isPlanet']:
                planets[body['englishName']] = {
                    'mass': body.get('mass', {}).get('massValue', 0),
                    'radius': body.get('meanRadius', 0),
                    'distance_from_sun': body.get('semimajorAxis', 0),  # in km
                    'gravity': body.get('gravity', 0),
                    'orbitalPeriod': body.get('sideralOrbit', 0), # in days
                }
        return planets