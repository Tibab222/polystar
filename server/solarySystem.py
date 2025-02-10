import datetime
import json
from calculations import *
from classes.planet_class import Planet
from astroquery.jplhorizons import Horizons

def getPlanetData():
    """
    Retrieves and sorts planets by their distance from the Sun.

    Returns:
        dict: A dictionary where the keys are planet names, and the values are dictionaries 
              containing planet attributes : name, mass, radius, distance from sun, gravity, and orbital period.
    """
    with open("solarySystemConsts.json") as f:
        data = json.load(f)
        planets = []
        for body in data['bodies']:
            if body['isPlanet']:
                planets.append({
                    'name': body['englishName'],
                    'mass': body.get('mass', {}).get('massValue', 0) * 1e24,  # Convert to kg
                    'radius': body.get('meanRadius', 0),  # in meters
                    'distance_from_sun': body.get('semimajorAxis', 0) * 1e3,  # Convert km to meters
                    'gravity': body.get('gravity', 0),  # in m/s²
                    'orbitalPeriod': body.get('sideralOrbit', 0),  # in days
                })
        # Sort planets by their distance from the Sun
        planets.sort(key=lambda x: x['distance_from_sun'])  
        return {p['name']: p for p in planets}
    
def buildPlanets():
    """
    Constructs Planet objects using planetary data.

    Returns:
        list: A list of `Planet` objects representing each celestial body.
    """
    planets = getPlanetData()
    planetsObjects = [
        Planet(name, 
            data["radius"], 
            data["mass"], 
            data["distance_from_sun"], 
            data["gravity"], 
            data["orbitalPeriod"],
            getPlanetAngle(name))  # Get initial angular position
        for name, data in planets.items()
    ]
    return planetsObjects

def getPlanetAngle(planetName):
    """
    Computes the initial angle of a planet relative to the x-axis.

    Uses the planet's current position retrieved from `getPlanetPosition()`
    to compute its angle using the `atan2(y, x)` function.

    Returns:
        float: The angle in radians relative to the x-axis.
    """
    pos = getPlanetPosition(planetName, datetime.datetime.now(datetime.timezone.utc))
    angleXY = math.atan2(pos["y"], pos["x"])
    return angleXY

def buildPlanet(planetName):
    """
    Constructs a `Planet` object for a given planet name.

    Returns:
        Planet: A `Planet` object with the retrieved properties.
    """
    planets = getPlanetData()
    p = planets[planetName]
    return Planet(p['name'], p['radius'], p['mass'], p['distance_from_sun'], p['gravity'], p['orbitalPeriod'])

def getPlanetIds():
    """
    Returns a dictionary mapping planet names to their JPL Horizons ID.

    Returns:
        dict: A dictionary where keys are planet names and values are their JPL Horizons IDs.
    """
    return {
        "Earth": "399", 
        "Moon": "301",
        "Mars": "499",
        "Jupiter": "599",
        "Venus": "299",
        "Mercury": "199",
        "Neptune": "899",
        "Saturn": "699",
        "Uranus": "799"
    }

def getPlanetPosition(planet_name, date_time):
    """
    Retrieves the real-time heliocentric (x, y, z) coordinates of a planet.

    Queries NASA JPL Horizons API using `astroquery.jplhorizons` to get the 
    planetary position at a specific date.

    Returns:
        dict: A dictionary containing:
              - "x", "y", "z": Coordinates in meters.
              - "gravity": The planet's gravitational acceleration.
    """
    planet_ids = getPlanetIds()
    planet_id = planet_ids[planet_name]  
    planet_data = getPlanetData()

    # Convert current datetime to Julian Date (JD)
    jd_now = date_time.timestamp() / 86400 + 2440587.5 

    # Query planetary position data from NASA JPL Horizons
    obj = Horizons(id=planet_id, location='500@0', epochs=[jd_now], id_type='majorbody')
    eph = obj.vectors()

    # Convert AU (astronomical units) to meters
    x = eph['x'][0] * 1.496e+11  
    y = eph['y'][0] * 1.496e+11
    z = eph['z'][0] * 1.496e+11  

    return {"x": x, "y": y, "z": z, "gravity": planet_data[planet_name]["gravity"]} 

def getPlanetsPositions():
    """
    Retrieves the real-time positions of all planets in the solar system.

    Returns:
        dict: A dictionary where keys are planet names and values are dictionaries containing:
              - "x", "y", "z" (coordinates in meters).
              - "gravity" (gravitational acceleration in m/s²).
    """
    date_time = datetime.datetime.now(datetime.timezone.utc)
    planets = getPlanetData()
    positions = {name: getPlanetPosition(name, date_time) for name in planets}
    return positions
