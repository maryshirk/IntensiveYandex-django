from django.test import Client, TestCase


# Create your tests here.
class StaticUrlTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get("/catalog/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_int_endpoint(self):
        response = Client().get("/catalog/1/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_re_int_endpoint(self):
        response = Client().get("/catalog/re/1/")
        self.assertEqual(response.status_code, 200)
