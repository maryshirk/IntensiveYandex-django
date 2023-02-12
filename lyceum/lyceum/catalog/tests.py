from django.test import Client, TestCase


# Create your tests here.
class StaticUrlTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get("/catalog/")
        self.assertEqual(response.status_code, 200)
