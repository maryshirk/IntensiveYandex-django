from django.test import Client, TestCase


class StaticUrlTests(TestCase):
    def test_coffee_endpoint(self):
        response = Client().get("/coffee/")
        self.assertEqual(response.status_code, 418)

    def test_coffee_contest_endpoint(self):
        response = Client().get("/coffee/")
        self.assertEqual(response.content.decode(), "<body>Я чайник</body>")
