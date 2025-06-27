import unittest
from city_functions import cityAndCountry

class CityTestCase(unittest.TestCase):
    def test_city_country(self):
        result = cityAndCountry("santiago", "chile")
        self.assertEqual(result, "Santiago, Chile")

unittest.main()