from django.test import TestCase
from django.utils.text import slugify
from products.models import Product, Category, Colour

class TestProductsModels(TestCase):

    def setUp(self):

        new_category = Category.objects.create(
            name='test_category', 
            slug='test-category', 
            friendly_name='test category',
        )

        new_product = Product.objects.create(
            category=new_category,
            product_name='test product',
            price=1
            )

        new_colour = Colour.objects.create(
            product=new_product,
            colour='test colour',
            hex_value='000'
        )
        
    """ Tests for Category Model Methods """

    def test_category_str_method(self):
        new_category = Category.objects.get(name='test_category')

        self.assertEqual(str(new_category), 'test_category')

    def test_category_get_friendly_name_method(self):
        new_category = Category.objects.get(name='test_category')
        expected_result = new_category.friendly_name
        result = Category.get_friendly_name(new_category)

        self.assertEqual(result, expected_result)
    
    def test_category_get_absolute_url_method(self):
        new_category = Category.objects.get(name='test_category')
        expected_result = '/products/' + new_category.slug + '/'
        result = Category.get_absolute_url(new_category)

        self.assertEqual(result, expected_result)

    """ Tests for Product Model Methods """

    def test_product_str_method(self):
        new_product = Product.objects.get(product_name='test product')

        self.assertEqual(str(new_product), 'test product')
    
    def test_product_save_method(self):
        new_product = Product.objects.get(product_name='test product')
        expected_result = slugify(new_product.product_name)
        result = new_product.slug
        
        self.assertEqual(result, expected_result)

    def test_product_get_absolute_url_method(self):
        new_category = Category.objects.get(name='test_category')
        new_product = Product.objects.get(product_name='test product')
        expected_result = '/products/' + new_category.slug + '/' + new_product.slug + '/'
        result = Product.get_absolute_url(new_product)

        self.assertEqual(result, expected_result)

    """ Tests for Colour Model Methods """
    
    def test_colour_str_method(self):
        new_colour = Colour.objects.get(colour='test colour')

        self.assertEqual(str(new_colour), 'test colour')

    def test_colour_get_hex_value_method(self):
        new_colour = Colour.objects.get(colour='test colour')
        result = Colour.get_hex_value(new_colour)

        self.assertEqual(result, '000')

    def tearDown(self):
        new_category = Category.objects.get(name='test_category')
        new_product = Product.objects.get(product_name='test product')
        new_colour = Colour.objects.get(colour='test colour')

        del new_category
        del new_product
        del new_colour