from catalog.models import Category, Item, Tag
from django.core.exceptions import ValidationError
from django.test import Client, TestCase


# Create your tests here.
class StaticUrlTests(TestCase):
    def test_catalog_endpoint(self):
        response = Client().get("/catalog/")
        self.assertEqual(response.status_code, 200)

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

    def test_catalog_re_zero_endpoint(self):
        response = Client().get("/catalog/re/0/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_re_negative_endpoint(self):
        response = Client().get("/catalog/re/-3/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_re_str_endpoint(self):
        response = Client().get("/catalog/re/fgpsdj/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_convert_endpoint(self):
        response = Client().get("/catalog/2222/3/")
        self.assertEqual(response.status_code, 200)

    def test_catalog_convert_date_endpoint(self):
        response = Client().get("/catalog/20224/3/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_convert_date_negative_endpoint(self):
        response = Client().get("/catalog/21224/-4/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_convert_negative_endpoint(self):
        response = Client().get("/catalog/2222/-4/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_convert_date_str_endpoint(self):
        response = Client().get("/catalog/dgfr/4/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_convert_str_endpoint(self):
        response = Client().get("/catalog/2122/sghgd/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_convert_str_str_endpoint(self):
        response = Client().get("/catalog/dgfr/fhth/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_convert_formatdate_endpoint(self):
        response = Client().get("/catalog/yyyymmdd/4/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_convert_data_double_endpoint(self):
        response = Client().get("/catalog/21221212/4.3/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_convert_data_zero_endpoint(self):
        response = Client().get("/catalog/1111/0/")
        self.assertEqual(response.status_code, 404)

    def test_catalog_convert_double_endpoint(self):
        response = Client().get("/catalog/2022/4.3/")
        self.assertEqual(response.status_code, 404)


class ModelTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            name="Тестовая категория",
            slug="test-category-slug",
        )
        cls.tag = Tag.objects.create(
            name="Тестовый тег",
            slug="test-tag-slug",
        )

    def test_without_needed_words(self):
        item_count = Item.objects.count()
        text_endpoints = [
            "какая-то бессмыслица",
            "нероскошно",
            "превосходность",
        ]
        for text in text_endpoints:
            Item.objects.all().delete()
            with self.subTest(
                 f"This word must fail validation"
                 f" - '{text}'"
                 ):
                with self.assertRaises(ValidationError):

                    self.item = Item(
                        name="товар номер 1",
                        category=self.category,
                        text=text,
                    )
                    self.item.full_clean()
                    self.item.save()
                    self.item.tags.add(self.tag)

                self.assertEqual(Item.objects.count(), item_count)

    def test_with_needed_words(self):
        item_count = Item.objects.count()
        text_endpoints = [
            "превосходно в нем все",
            "это роскошно,превосходно",
            "Это роскошно!",
        ]
        for text in text_endpoints:
            Item.objects.all().delete()
            with self.subTest(
                 f"The model Item with such text must be created"
                 f" - '{text}'"
                 ):

                self.item = Item(
                    name="тестовый товар",
                    category=self.category,
                    text=text,
                )
                self.item.full_clean()
                self.item.save()
                self.item.tags.add(self.tag)
                self.assertEqual(Item.objects.count(), item_count + 1)
