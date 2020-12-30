from django.test import TestCase
from products.models import Product, Category, Colour

class TestProductsModels(TestCase):

    """ Tests for Category Model Methods """

    def test_category_str_method(self):
        new_category = Category.objects.create(
            name="test_category", slug="test-category", friendly_name="test category",
        )
        self.assertEqual(str(new_category), "test_category")
        self.assertEqual(str(new_category.slug), "test-category")
        self.assertEqual(str(new_category.get_friendly_name()), "test category")

    def test_category_get_friendly_name_method(self):
        new_category = Category.objects.create(
            name="test_category", slug="test-category", friendly_name="test category",
        )
        expected_result = new_category.friendly_name
        result = Category.get_friendly_name(new_category)

        self.assertEqual(result, expected_result)

    def test_category_get_absolute_url_method(self):
        new_category = Category.objects.create(
            name="test_category", slug="test-category", friendly_name="test category",
        )
        expected_result = '/products/' + new_category.slug + '/'
        result = Category.get_absolute_url(new_category)

        self.assertEqual(result, expected_result)
