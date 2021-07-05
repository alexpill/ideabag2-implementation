from src.distance_between_2_cities import *
import unittest

class HaversineTest(unittest.TestCase):
    def test_distance(self):
        city1 = [48.8568, 2.3514] # Paris, France

        # Status of Liberty, Manhattan, New York, USA
        city2 = [40.71248, -74.00511]

        dist = Haversine(city1, city2)
        self.assertAlmostEqual(dist.kilometers, 5837, places=0)

class CityFinderTest(unittest.TestCase):
    def test_valid_city_finder(self):
        coord = get_city_coordinates("Paris")
        ref_coord = [48.8566969, 2.3514616]
        self.assertEqual(coord, ref_coord)

    def test_invalid_city_finder(self):
        with self.assertRaises(CityNotFoundError):
            get_city_coordinates("qwertyuiop")


if __name__ == '__main__':
    unittest.main()
