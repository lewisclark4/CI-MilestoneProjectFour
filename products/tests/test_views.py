from django.test import TestCase
from products.models import Product, Category, Colour

# Create your tests here.

class TestProductsViews(TestCase):
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
    
    def test_all_products_view(self):
        response = self.client.get("/products/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_category_view(self):
        response = self.client.get("/products/test-category/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/products.html")

    def test_product_details_view(self):
        new_category = Category.objects.get(name='test_category')
        new_product = Product.objects.get(product_name='test product')
        url = Product.get_absolute_url(new_product)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "products/product_detail.html")

    def tearDown(self):
        new_category = Category.objects.get(name='test_category')
        new_product = Product.objects.get(product_name='test product')
        new_colour = Colour.objects.get(colour='test colour')

        del new_category
        del new_product
        del new_colour