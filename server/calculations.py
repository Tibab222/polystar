import math

def orbital_speed(orbital_radius, mass, GRAVITY):
    """
    Calculates the orbital speed of a planet.

    This function uses the formula for orbital velocity, derived from Newton's 
    law of universal gravitation and centripetal force.

    Formula:
        v = sqrt(G * M / r)

    Returns:
        float: The orbital speed of the object in meters per second (m/s).
    """
    return math.sqrt(GRAVITY * mass / orbital_radius)

def orbital_period(orbital_radius, mass, GRAVITY):
    """
    Calculates the orbital period of a planet.

    This function applies Kepler's Third Law.

    Formula:
        T = 2 * π * r / v

    Returns:
        float: The time taken for a full orbit in seconds (s).
    """
    return 2 * math.pi * orbital_radius / orbital_speed(orbital_radius, mass, GRAVITY)

def average_planet_speed(distanceFromSun, period_in_days):
    """
    Calculates the average orbital speed of a planet around the Sun.

    Formula:
        v = 2 * π * r / T

    Returns:
        float: The average orbital speed of the planet in meters per second (m/s).
    """
    return distanceFromSun * 2 * math.pi / (period_in_days * 24 * 3600)  # Convert days to seconds


