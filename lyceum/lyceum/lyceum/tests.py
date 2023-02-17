from django.test import Client, TestCase

from lyceum.settings import REVERSE_FLAG


reverse_flag = REVERSE_FLAG
# Create your tests here.


class StaticUrlTests(TestCase):
    def test_middleware_coffee(self):
        if reverse_flag is True:
            n = 0
            for i in range(10):
                response = Client().get("/coffee/")
                r = response.content.decode()
                s = "<body>" + r[6:-7][::-1] + "</body>"
                if r != s:
                    n += 1
            self.assertEqual(n, 10)
        else:
            n = 0
            for i in range(10):
                response = Client().get("/coffee/")
                r = response.content.decode()
                s = "<body>" + r[6:-7][::-1] + "</body>"
                if r != s:
                    n += 1
            self.assertEqual(n, 10)

    def test_middleware_catalog(self):
        if reverse_flag is True:
            n = 0
            for i in range(10):
                response = Client().get("/catalog/3/")
                r = response.content.decode()
                s = "<body>" + r[6:-7][::-1] + "</body>"
                if r != s:
                    n += 1
            self.assertEqual(n, 10)
        else:
            n = 0
            for i in range(10):
                response = Client().get("/catalog/4/")
                r = response.content.decode()
                s = "<body>" + r[6:-7][::-1] + "</body>"
                if r != s:
                    n += 1
            self.assertEqual(n, 10)

    def test_middleware_about(self):
        if reverse_flag is True:
            n = 0
            for i in range(10):
                response = Client().get("/about/")
                r = response.content.decode()
                s = "<body>" + r[6:-7][::-1] + "</body>"
                if r != s:
                    n += 1
            self.assertEqual(n, 10)
        else:
            n = 0
            for i in range(10):
                response = Client().get("/about/")
                r = response.content.decode()
                s = "<body>" + r[6:-7][::-1] + "</body>"
                if r != s:
                    n += 1
            self.assertEqual(n, 10)

    def test_middleware(self):
        n = 0
        for i in range(10):
            response = Client().get("/catalog/dgrgfd")
            if response.status_code == 404:
                n += 1
        self.assertEqual(n, 10)
