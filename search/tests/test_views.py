from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.messages import get_messages
from products.models import Product, Category
from django.db.models import Q


class TestSearchViews(TestCase):
    def setUp(self):

        new_category = Category.objects.create(
            name='test_category',
            slug='test-category',
            friendly_name='test category',
        )

        Product.objects.create(
            category=new_category,
            brand_name='test brand',
            product_name='test product',
            description='test description',
            price=1
            )

    def test_search_view(self):
        response = self.client.post(reverse('search'), follow=True)
        self.assertRedirects(response, '/products/')

    def test_search_by_product_name(self):
        url = '/search/?q=test+product'
        query = 'test product'
        response = self.client.get(url)
        search_result = Product.objects.all().filter(Q(
                            product_name__contains=query))

        self.assertQuerysetEqual(
            response.context['products'], search_result, transform=lambda a: a)

    def test_search_by_brand_name(self):
        url = '/search/?q=test+brand'
        query = 'test brand'
        response = self.client.get(url)
        search_result = Product.objects.all().filter(Q(
                            brand_name__contains=query))

        self.assertQuerysetEqual(
            response.context['products'], search_result, transform=lambda a: a)

    def test_search_by_category(self):
        url = '/search/?q=test+category'
        query = 'test category'
        response = self.client.get(url)
        search_result = Product.objects.all().filter(Q(
                            category__friendly_name__contains=query))

        self.assertQuerysetEqual(
            response.context['products'], search_result, transform=lambda a: a)

    def test_search_by_description(self):
        url = '/search/?q=test+description'
        query = 'test description'
        response = self.client.get(url)
        search_result = Product.objects.all().filter(Q(
                            description__contains=query))

        self.assertQuerysetEqual(
            response.context['products'], search_result, transform=lambda a: a)

    def test_error_message_blank_search(self):
        url = '/search/?q='
        response = self.client.get(url)
        expected_message = 'Please enter a search criteria'
        messages = list(get_messages(response.wsgi_request))

        self.assertEqual(messages[0].tags, 'warning')
        self.assertEqual(str(messages[0]), expected_message)


    def test_no_search_results(self):
        q = {
            'q' :  '123456789'    
        }
        response = self.client.get(reverse('search'), q, follow=True)
        expected_message = f"There were no results found for the search: {q['q']}."
        messages = list(get_messages(response.wsgi_request))
        
        self.assertRedirects(response, '/products/')
        self.assertEqual(messages[0].tags, 'warning')
        self.assertEqual(str(messages[0]), expected_message)
        

    def tearDown(self):
        new_category = Category.objects.get(name='test_category')
        new_product = Product.objects.get(product_name='test product')

        del new_category
        del new_product
