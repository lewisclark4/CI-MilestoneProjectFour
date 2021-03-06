from django.test import TestCase
from products.models import Product, Category, Colour


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

        Colour.objects.create(
            product=new_product,
            colour='test colour',
            hex_value='000'
        )

    def test_all_products_view(self):
        response = self.client.get('/products/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_all_products_sort_price_asc(self):
        response = self.client.get('/products/?sort=price&direction=asc')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_all_products_sort_price_desc(self):
        response = self.client.get('/products/?sort=price&direction=desc')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_category_view(self):
        new_category = Category.objects.get(name='test_category')
        response = self.client.get('/products/' + new_category.slug + '/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_category_sort_price_asc(self):
        new_category = Category.objects.get(name='test_category')
        response = self.client.get('/products/' + new_category.slug
                                   + '/' + '?sort=price&direction=asc')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_category_sort_price_desc(self):
        new_category = Category.objects.get(name='test_category')
        response = self.client.get('/products/' + new_category.slug + '/'
                                   + '?sort=price&direction=desc')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_featured_products_view(self):
        response = self.client.get('/products/featured/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_feautred_product_sort_price_asc(self):
        Category.objects.get(name='test_category')
        response = self.client.get(
                            '/products/featured/?sort=price&direction=asc')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_feautred_product_sort_price_desc(self):
        Category.objects.get(name='test_category')
        response = self.client.get(
                            '/products/featured/?sort=price&direction=desc')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_details_view(self):
        new_product = Product.objects.get(product_name='test product')
        url = Product.get_absolute_url(new_product)
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')

    def tearDown(self):
        new_category = Category.objects.get(name='test_category')
        new_product = Product.objects.get(product_name='test product')
        new_colour = Colour.objects.get(colour='test colour')

        del new_category
        del new_product
        del new_colour
