from django.core.exceptions import ValidationError
from django.test import Client, TestCase
from django.urls import reverse

from catalog.models import Category, Item, Tag


class StaticUrlTests(TestCase):
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
                f"This word must fail validation" f" - '{text}'"
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
                f"The model Item with such text must be created" f" - '{text}'"
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


class TaskPagesTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.category = Category.objects.create(
            name='Тестовая категория',
            slug='test-category-slug',
        )
        Item.objects.create(
            name='Test item 1',
            text='превосходно',
            category=cls.category,
            is_published=True,
        )
        Item.objects.create(
            name='Test item 2',
            text='роскошно',
            category=cls.category,
            is_published=False,
        )
        Item.objects.create(
            name='Test item 3',
            text='превосходно',
            category=cls.category,
            is_published=True,
        )

    def test_catalog_shown_correct_context_item_list(self):
        response = Client().get(reverse('catalog:item_list'))
        self.assertIn('items', response.context)

    def test_catalog_shown_correct_context_item_detail(self):
        response = Client().get(reverse('catalog:item_detail', args=[1]))
        self.assertIn('item', response.context)

    def test_catalog_count_publisheditems(self):
        response = Client().get(reverse('catalog:item_list'))
        self.assertEqual(len(response.context['items']), 2)


class ContextTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        cls.published_category = Category.objects.create(
            is_published=True,
            name="Тестовая опубликованная категория",
            slug="published_category",
            weight=100,
        )

        cls.unpublished_category = Category.objects.create(
            is_published=False,
            name="Тестовая неопубликованная категория",
            slug="unpublished_category",
            weight=100,
        )

        cls.published_tag = Tag.objects.create(
            is_published=True,
            name="Тестовый опубликованный тэг",
            slug="published_tag",
        )

        cls.unpublished_tag = Tag.objects.create(
            is_published=False,
            name="Тестовый неопубликованный тэг",
            slug="unpublished_tag",
        )

        cls.unpublished_item = Item(
            name="Непубликованный товар",
            category=cls.published_category,
            text="превосходно",
            is_published=False,
        )

        cls.published_item = Item(
            name="Опубликованный товар",
            category=cls.published_category,
            text="превосходно",
        )

        cls.published_category.save()
        cls.unpublished_category.save()

        cls.published_tag.save()
        cls.unpublished_tag.save()

        cls.published_item.clean()
        cls.published_item.save()
        cls.unpublished_item.clean()
        cls.unpublished_item.save()

        cls.published_item.tags.add(cls.published_tag.pk)
        cls.published_item.tags.add(cls.unpublished_tag.pk)

        def test_homepage_show_correct_context(self):
            response = Client().get(reverse('homepage:home'))
            self.assertIn('items', response.context)

        def test_catalog_queryset(self):
            response = Client().get(reverse('catalog:item_list'))
            self.assertIn(
                self.published_item,
                response.context["items"],
            )
            self.assertNotIn(
                self.unpublished_item,
                response.context["items"],
            )

        def test_count_publisheditems(self):
            response = Client().get(reverse('catalog:item_list'))
            self.assertEqual(len(response.context['items']), 1)
