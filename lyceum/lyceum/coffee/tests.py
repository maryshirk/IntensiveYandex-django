from django.test import Client, TestCase


# Create your tests here.
class StaticUrlTests(TestCase):
    def test_coffee_endpoint(self):
        response = Client().get("/")
        self.assertEqual(response.status_code, 418)

    def test_coffee_content(self):
        response = Client().get("/")
        self.assertEqual(response.content, "<body>Я чайник</body>")
