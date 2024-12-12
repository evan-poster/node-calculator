import unittest
import requests

BASE_URL = "http://localhost:3001"

class TestAPIEndpoints(unittest.TestCase):
    def test_root(self):
        response = requests.get(f"{BASE_URL}/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Hello from the backend!"})

    def test_add(self):
        response = requests.get(f"{BASE_URL}/add", params={"n1": 5, "n2": 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 8})

        # Test error case
        response = requests.get(f"{BASE_URL}/add", params={"n1": "a", "n2": 3})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Both n1 and n2 must be numbers."})

    def test_subtract(self):
        response = requests.get(f"{BASE_URL}/subtract", params={"n1": 5, "n2": 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 2})

        # Test error case
        response = requests.get(f"{BASE_URL}/subtract", params={"n1": 5, "n2": "b"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Both n1 and n2 must be numbers."})

    def test_multiply(self):
        response = requests.get(f"{BASE_URL}/multiply", params={"n1": 5, "n2": 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 15})

        # Test error case
        response = requests.get(f"{BASE_URL}/multiply", params={"n1": "c", "n2": "d"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Both n1 and n2 must be numbers."})

    def test_divide(self):
        response = requests.get(f"{BASE_URL}/divide", params={"n1": 6, "n2": 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 2})

        # Test division by zero
        response = requests.get(f"{BASE_URL}/divide", params={"n1": 5, "n2": 0})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Cannot divide by zero."})

        # Test error case
        response = requests.get(f"{BASE_URL}/divide", params={"n1": "e", "n2": 3})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Both n1 and n2 must be numbers."})

    def test_power(self):
        response = requests.get(f"{BASE_URL}/power", params={"n1": 2, "n2": 3})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 8})

        # Test error case
        response = requests.get(f"{BASE_URL}/power", params={"n1": 2, "n2": "f"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Both n1 and n2 must be numbers."})

    def test_root(self):
        response = requests.get(f"{BASE_URL}/root", params={"n1": 9})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 3})

        # Test negative number
        response = requests.get(f"{BASE_URL}/root", params={"n1": -4})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "n1 must be a positive number."})

        # Test error case
        response = requests.get(f"{BASE_URL}/root", params={"n1": "g"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "n1 must be a number."})

    def test_square(self):
        response = requests.get(f"{BASE_URL}/square", params={"n1": 4})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"result": 16})

        # Test error case
        response = requests.get(f"{BASE_URL}/square", params={"n1": "h"})
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "n1 must be a number."})

if __name__ == "__main__":
    unittest.main()
