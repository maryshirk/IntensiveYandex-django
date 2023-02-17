from django.conf import settings
from django.test import Client, TestCase


reverse_flag = settings.REVERSE_FLAG
# Create your tests here.


class StaticUrlTests(TestCase):
    def test_middleware(self):
        if reverse_flag is True:
            reverse_flag = False
            client_self = Client()
            n = 0
            for _ in range(10):
                client_self.get("/coffee/")
                response = client_self.get("/coffee/")
                if response.content.decode() == "Я кинйач":
                    n += 1
            self.assertEqual(n, 0)
        else:
            reverse_flag = True
            client_self = Client()
            n = 0
            for _ in range(10):
                client_self.get("/coffee/")
                response = client_self.get("/coffee/")
                if response.content.decode() == "Я кинйач":
                    n += 1
            self.assertEqual(n, 1)
