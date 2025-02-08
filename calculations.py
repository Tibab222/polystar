import math

def orbital_speed(orbital_radius, mass, GRAVITY):
    """
    Vitesse orbitale d'un objet en orbite circulaire autour d'un corps massif.
    @param orbital_radius: rayon de l'orbite (m)
    @param mass: masse du corps massif (kg)
    @param GRAVITY: constante gravitationnelle (m^3 kg^-1 s^-2)
    """
    return math.sqrt(GRAVITY * mass / orbital_radius)

def orbital_period(orbital_radius, mass, GRAVITY):
    """Période orbitale d'un objet en orbite circulaire autour d'un corps massif. 3eme loi de Kepler."""
    return 2 * math.pi * orbital_radius / orbital_speed(orbital_radius, mass, GRAVITY)

def average_planet_speed(distanceFromSun, period_in_days):
    """
        Vitesse orbitale moyenne d'une planete autour du Soleil.
        @param distanceFromSun: distance moyenne de la planete au Soleil (km)
        @param period_in_days: periode orbitale de la planete pour faire un tour autour du soleil (jours)
    """
    return distanceFromSun * 2 * math.pi / (period_in_days * 24 * 3600)


