from django.conf import settings
from django.test import Client, TestCase


class StaticUrlTests(TestCase):
    def test_middleware_positive(self):
        if settings.REVERSE_FLAG is True:
            settings.REVERSE_FLAG = False
            client_self = Client()
            n = 0
            for _ in range(10):
                client_self.get("/coffee/")
                response = client_self.get("/coffee/")
                if response.content.decode() == "Я кинйач":
                    n += 1
            self.assertEqual(n, 0)

    def test_middleware_negative(self):
        if settings.REVERSE_FLAG is False:
            settings.REVERSE_FLAG = True
            client_self = Client()
            n = 0
            for _ in range(10):
                client_self.get("/coffee/")
                response = client_self.get("/coffee/")
                if response.content.decode() == "Я кинйач":
                    n += 1
            self.assertEqual(n, 1)
