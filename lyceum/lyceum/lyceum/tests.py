from django.test import Client, TestCase

from lyceum.settings import REVERSE


# Create your tests here.
class StaticUrlTests(TestCase):
    def test_middleware_coffee(self):
        if REVERSE is True:
            n = 0
            for i in range(10):
                response = Client().get("/coffee/")
                r = response.content.decode()
                s = "<body>" + r[6:-7][::-1] + "</body>"
                if r != s:
                    n += 1
            self.assertEqual(n, 1)
        else:
            n = 0
            for i in range(10):
                response = Client().get("/coffee/")
                r = response.content.decode()
                s = "<body>" + r[6:-7][::-1] + "</body>"
                if r != s:
                    n += 1
            self.assertEqual(n, 0)

    def test_middleware_catalog(self):
        if REVERSE is True:
            n = 0
            for i in range(10):
                response = Client().get("/catalog/3/")
                r = response.content.decode()
                s = "<body>" + r[6:-7][::-1] + "</body>"
                if r != s:
                    n += 1
            self.assertEqual(n, 1)
        else:
            n = 0
            for i in range(10):
                response = Client().get("/catalog/4/")
                r = response.content.decode()
                s = "<body>" + r[6:-7][::-1] + "</body>"
                if r != s:
                    n += 1
            self.assertEqual(n, 0)

    def test_middleware_about(self):
        if REVERSE is True:
            REVERSE = False
            n = 0
            for i in range(10):
                response = Client().get("/about/")
                r = response.content.decode()
                s = "<body>" + r[6:-7][::-1] + "</body>"
                if r != s:
                    n += 1
            REVERSE = True
            self.assertEqual(n, 0)
        else:
            REVERSE = True
            n = 0
            for i in range(10):
                response = Client().get("/about/")
                r = response.content.decode()
                s = "<body>" + r[6:-7][::-1] + "</body>"
                if r != s:
                    n += 1
            REVERSE = False
            self.assertEqual(n, 1)

    def test_middleware(self):
        if REVERSE is True:
            n = 0
            for i in range(10):
                response = Client().get("/catalog/fdhdhd/")
                if response.status_code == 404:
                    n += 1
            self.assertEqual(n, 10)
        else:
            REVERSE = True
            n = 0
            for i in range(10):
                response = Client().get("/catalog/rturur/")
                if response.status_code == 404:
                    n += 1
            REVERSE = False
            self.assertEqual(n, 10)
