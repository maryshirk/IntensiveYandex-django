from django.test import Client, TestCase


# Create your tests here.
class StaticUrlTests(TestCase):
    def test_coffee_endpoint(self):
        response = Client().get("/coffee/")
        self.assertEqual(response.status_code, 418)
