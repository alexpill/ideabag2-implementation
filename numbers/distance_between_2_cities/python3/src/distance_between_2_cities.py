#!/usr/bin/env python3

"""Calculated the distance between 2 cities

This script calculates the distance between 2 cities, using the Haversine
formula. This method might not be the best and the most accurate but it is quite
simple to implement.
"""

from math import sin, cos, asin, sqrt, radians
import requests

__author__ = "Alexandre Pilleyre"
__copyright__ = "Copyright 2021, Alexandre Pilleyre"
__credits__ = ["Alexandre Pilleyre", "mclintprojects"]
# mclintprojects for providing IdeaBag2 app

__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Alexandre Pilleyre"
__email__ = ""  # TODO: fill
__status__ = "Dev"

EARTH_MEAN_RADIUS = 6371000 # meters

class CityNotFoundError(Exception):
    """Custom error with meaningful name"""
    pass

def get_city_coordinates(city_name):
    """ Gets the coordinates of a city or a place

    Returns the coordinates under the format [latitude, longitude] from a city
    or a place name using the nominatim from openstreetmap.org

    @param city_name: name of the city (or place) to find
    @type city_name: str

    @return: the coordinates of the city ([latitude, longitude])
    @rtype: list
    """

    #TODO: clean & verif input city name
    base_url = "https://nominatim.openstreetmap.org/search?city="
    url = f"{base_url}{city_name}&format=json"
    req = requests.get(url)
    values = req.json()
    if values == []:
        raise CityNotFoundError(f"'{city_name}' not found")
    first_city = values[0]
    lat = float(first_city['lat'])
    long = float(first_city['lon'])
    return [lat, long]

class Haversine:
    """Simple haversine method resolution

    Allows to compute the distance between two points on the surface of a sphere.
    By default, the radius of the sphere is the mean radius of the Earth so by
    default the class gives the distance between two coordinates (for example
    cities) between those two points.
    The coordinates of the points are given in decimal degrees (DD).
    """
    def __init__(self, coord1, coord2, radius=EARTH_MEAN_RADIUS):
        """
        @param coord1: coordinates of the point (lat, long in DD)
        @param coord2: coordinates of the second point (lat, long in DD)
        @param radius: radius of the sphere

        @type coord1: list
        @type coord2: list
        @type radius: float
        """
        if len(coord1) != 2 or len(coord2) != 2:
            raise ValueError("The coords must the [latitude, longitude] format")

        # see https://en.wikipedia.org/wiki/Haversine_formula
        def haversine(lt1, lg1, lt2, lg2, r):
            phi1 = radians(lt1)
            phi2 = radians(lt2)
            delta_phi = phi2 - phi1
            delta_lambda = radians(lg2 - lg1)

            return 2 * r * \
                asin(sqrt(
                    sin(delta_phi / 2) ** 2 + \
                        cos(phi1) * cos(phi2) * sin(delta_lambda / 2) ** 2
                    )
                )

        distance = haversine(*coord1, *coord2, radius)

        self.meters = distance
        self.kilometers = distance / 1000
        self.miles = distance * 0.000621371


def main():
    first_city = input("First city (or place): ")
    second_city = input("Second city (or place): ")

    first_coord = []
    second_coord = []

    try:
        first_coord = get_city_coordinates(first_city)
        second_coord = get_city_coordinates(second_city)
    except CityNotFoundError as error:
        print(f"Error: {error}")
        return

    distance = Haversine(first_coord, second_coord)

    print(f"Distance beetween '{first_city}' and '{second_city} is:'")
    print(f"\t{distance.meters} m")
    print(f"\t{distance.kilometers} km")
    print(f"\t{distance.miles} miles")



if __name__ == "__main__":
    main()
