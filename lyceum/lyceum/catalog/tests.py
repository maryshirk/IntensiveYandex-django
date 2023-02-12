from django.test import Client, TestCase


# Create your tests here.
class StaticUrlTests(TestCase):
    # /catalog/
    def test_catalog_endpoint(self):
        response = Client().get("/catalog/")
        self.assertEqual(response.status_code, 200)
    # /catalog/целое положительное число
    def test_catalog_int_endpoint(self):
        response = Client().get("/catalog/1/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_int2_endpoint(self):
        response = Client().get("/catalog/13/")
        self.assertEqual(response.status_code, 200)
    
    def test_catalog_int3_endpoint(self):
        response = Client().get("/catalog/134/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_double_endpoint(self):
        response = Client().get("/catalog/1.3/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_double2_endpoint(self):
        response = Client().get("/catalog/1,35/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_negative_endpoint(self):
        response = Client().get("/catalog/-3/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_str_endpoint(self):
        response = Client().get("/catalog/fhgdg/")
        self.assertEqual(response.status_code, 404)
    # /catalog/re/целое положительное число
    def test_catalog_re_int_endpoint(self):
        response = Client().get("/catalog/re/1/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_re_int2_endpoint(self):
        response = Client().get("/catalog/re/13/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_re_int3_endpoint(self):
        response = Client().get("/catalog/re/134/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_re_double_endpoint(self):
        response = Client().get("/catalog/re/1.3/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_re_double2_endpoint(self):
        response = Client().get("/catalog/re/1,34/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_re_negative_endpoint(self):
        response = Client().get("/catalog/re/-3/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_re_str_endpoint(self):
        response = Client().get("/catalog/re/fgpsdj/")
        self.assertEqual(response.status_code, 404)
    # /catalog/yyyy-mm-dd/целое положительное число/
    def test_catalog_convert_endpoint(self):
        response = Client().get("/catalog/2022-02-12/3")
        self.assertEqual(response.status_code, 200)

    def test_catalog_convert_date_endpoint(self):
        response = Client().get("/catalog/2022-0223-12/3")
        self.assertEqual(response.status_code, 404)

    def test_catalog_convert_date_negative_endpoint(self):
        response = Client().get("/catalog/2022-0223-12/-4")
        self.assertEqual(response.status_code, 404)

    def test_catalog_convert_negative_endpoint(self):
        response = Client().get("/catalog/2022-02-12/-4")
        self.assertEqual(response.status_code, 404)

    def test_catalog_convert_date_str_endpoint(self):
        response = Client().get("/catalog/dgfr/4")
        self.assertEqual(response.status_code, 404)

    def test_catalog_convert_str_endpoint(self):
        response = Client().get("/catalog/2022-02-12/sghgd")
        self.assertEqual(response.status_code, 404)

    def test_catalog_convert_str_str_endpoint(self):
        response = Client().get("/catalog/dgfr/fhth")
        self.assertEqual(response.status_code, 404)

    def test_catalog_convert_formatdate_endpoint(self):
        response = Client().get("/catalog/yyyy-mm-dd/4")
        self.assertEqual(response.status_code, 404)

    def test_catalog_convert_double_endpoint(self):
        response = Client().get("/catalog/2022-02-12/4.3")
        self.assertEqual(response.status_code, 404)
