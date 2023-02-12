from django.test import Client, TestCase


# Create your tests here.
class StaticUrlTests(TestCase):
    def test_coffee_endpoint(self):
        response = Client().get("/coffee/")
        self.assertEqual(response.status_code, 418)


    def test_coffee_content(self):
        response = Client().get("/coffee/")
        self.assertEqual(
            response.content,
            "<body>\xd0\xaf \xd1\x87"
            "\xd0\xb0\xd0\xb9\xd0\xbd\xd0\xb8\xd0\xba</body>"
        )
