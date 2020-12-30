from django.test import TestCase
from django.utils.text import slugify
from products.models import Product, Category, Colour

class TestProductsModels(TestCase):

    """ Tests for Category Model Methods """

    def test_category_str_method(self):
        new_category = Category.objects.create(
            name="test_category", 
        )
        self.assertEqual(str(new_category), "test_category")

    def test_category_get_friendly_name_method(self):
        new_category = Category.objects.create(
            name="test_category", 
            friendly_name="test category",
        )
        expected_result = new_category.friendly_name
        result = Category.get_friendly_name(new_category)

        self.assertEqual(result, expected_result)

    def test_category_get_absolute_url_method(self):
        new_category = Category.objects.create(
            name="test_category", 
            slug="test-category", 
            friendly_name="test category",
        )
        expected_result = '/products/' + new_category.slug + '/'
        result = Category.get_absolute_url(new_category)

        self.assertEqual(result, expected_result)


    """ Tests for Product Model Methods """

    def test_product_str_method(self):
        new_product = Product.objects.create(
            product_name="test product",
            price=1
        )
        self.assertEqual(str(new_product), "test product")

    def test_product_save_method(self):
        new_product = Product.objects.create(
            product_name="test product",
            price=1
        )
        expected_result = slugify(new_product.product_name)
        save = Product.save(new_product)
        product = Product.objects.get(product_name="test product")
        result = product.slug

        self.assertEqual(result, expected_result)

    def test_product_get_absolute_url_method(self):
        new_category = Category.objects.create(
            name="test_category", 
            slug="test-category", 
        )
        new_product = Product.objects.create(
            category=new_category,
            product_name="test product", 
            slug="test-product",
            price=1
            )
        
        expected_result = '/products/' + new_category.slug + '/' + new_product.slug + '/'
        result = Product.get_absolute_url(new_product)

        self.assertEqual(result, expected_result)

        """ Tests for Colour Model Methods """
    
    def test_colour_str_method(self):
        new_colour = Colour.objects.create(
            colour="test colour", 
        )
        self.assertEqual(str(new_colour), "test colour")

    def test_colour_get_hex_value_method(self):
        new_colour = Colour.objects.create(
            colour="test colour",
            hex_value="000"
        )
        self.assertEqual(str(new_colour.hex_value), "000")
