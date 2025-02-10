import math
import numpy as np

class Rocket:
    """
    Represents a spacecraft navigating through the solar system.

    This class models the movement of a rocket through space, including 
    fuel consumption, trajectory adjustments, and gravitational slingshot 
    maneuvers for optimizing fuel efficiency.
    """

    def __init__(self, name, speed, departure_planet):
        """
        Initializes the Rocket with its initial parameters.

        Args:
            name (str): The name of the rocket.
            speed (float): The initial speed of the rocket in meters per second (m/s).
            departure_planet (Planet): The planet from which the rocket departs.

        Attributes:
            name (str): The name of the rocket.
            speed (numpy.array): The velocity vector of the rocket (vx, vy).
            position (numpy.array): The initial position of the rocket based on the departure planet.
            gas (float): The remaining fuel percentage (initially 100%).
            time (float): The total elapsed time since departure.
            steps (list): A history of movements, storing visited planets, fuel levels, and positions.
            current_planet (Planet): The last visited planet.
        """
        self.name = name
        self.speed = np.array([speed, 0])  # Initial velocity (vx, vy)
        self.position = np.array(departure_planet.position_at_time(0))  # Initial position from the departure planet
        self.gas = 100  # Fuel (in %)
        self.time = 0  # Total elapsed time
        self.steps = []  # Movement history log

        # Store initial state in movement history
        self.steps.append({
            "planet": departure_planet.name,
            "position": self.position.tolist(),
            "fuel": self.gas,
            "time": self.time
        })

        self.current_planet = departure_planet  # Last visited planet

    def __str__(self):
        """

        Returns:
            str: A formatted string with the Rocket's name, position, and fuel level.
        """
        return f"{self.name} is at {self.position} with {self.gas}% fuel remaining"

    def get_planet_position_at_arrival(self, planet, time_elapsed):
        """
        Retrieves the expected position of a planet at the estimated time of arrival.

        Returns:
            numpy.array: The (x, y) position of the planet at the arrival time.
        """
        return np.array(planet.position_at_time(time_elapsed))

    def calculate_slingshot(self, planet):
        """
        Computes the new velocity after performing a gravitational slingshot maneuver.

        The function calculates the change in velocity based on the mass and gravity
        of the encountered planet, leveraging the planet's movement to gain additional speed.

        Returns:
            numpy.array: The new velocity vector of the rocket after the slingshot.
        """
        G = planet.gravity 
        impact_parameter = planet.radius * 1.5  # impact parameter for slingshot effect
        v_relative_in = self.speed - planet.averageSpeed  
        v_rel_norm = np.linalg.norm(v_relative_in) 

        # Here we calculate the deflection angle
        delta_theta = 2 * math.atan((G * planet.mass) / (impact_parameter * v_rel_norm ** 2))

        # The we apply a rotation matrix to adjust the speed direction
        cos_theta = math.cos(delta_theta)
        sin_theta = math.sin(delta_theta)
        rotation_matrix = np.array([[cos_theta, -sin_theta], [sin_theta, cos_theta]])
        v_relative_out = np.dot(rotation_matrix, v_relative_in)

        return v_relative_out + planet.averageSpeed 

    def move_to_planet(self, planet):
        """
        Moves the Rocket to the specified planet, adjusting velocity and fuel accordingly.

        The function calculates the time required to reach the planet, applies a 
        gravitational assist maneuver if applicable, and updates the Rocket's 
        fuel consumption based on the distance traveled.

        Returns:
            tuple: The distance traveled (meters) and the time taken (seconds).
        """
        self.gas -= 5  # Base fuel consumption per fligt

        # distance to the target planet
        distance = np.linalg.norm(self.position - planet.position_at_time(self.time))
        
        # time required to reach the planet
        time_to_reach = distance / np.linalg.norm(self.speed)  # in seconds

        # Here we get the planet's new position at the estimated time of arrival
        new_planet_position = self.get_planet_position_at_arrival(planet, time_to_reach)

        # We apply the slingshot => the planet's gravitational force boosts the speed of our rocket 
        new_speed = self.calculate_slingshot(planet)

        # Compute fuel consumption, scaled by the new speed and distance traveled
        fuel_consumption = (distance / 10000) / np.linalg.norm(new_speed) * 0.2 # This is an arbitrary factor
        
        self.position = new_planet_position
        self.speed = new_speed
        self.gas -= (fuel_consumption - 100) / 100
        self.time += time_to_reach
        self.current_planet = planet

        # Store movement data in history log
        self.steps.append({
            "planet": planet.name,
            "position": self.position.tolist(),
            "speed": self.speed.tolist(),
            "fuel": self.gas,
            "time": self.time
        })

        return distance, time_to_reach
