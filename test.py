import unittest
import requests

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        """Set up the base URL for testing."""
        self.base_url = "http://localhost:5000"

    def test_hello_world(self):
        """Test the home page of the Flask app."""
        response = requests.get(self.base_url + "/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.text, "Hello, World!")

if __name__ == '__main__':
    unittest.main()
