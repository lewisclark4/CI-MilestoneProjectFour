from django.test import TestCase
from django.contrib.messages import get_messages
from django.shortcuts import reverse
from checkout.models import Order, OrderLineItem
from products.models import Product, Category, Colour


class TestCheckoutViews(TestCase):

    def setUp(self):
        new_category = Category.objects.create(
            name='test_category',
            slug='test-category',
            friendly_name='test category',
        )

        new_product = Product.objects.create(
            category=new_category,
            product_name='test product',
            price=1.00
            )

        Colour.objects.create(
            product=new_product,
            colour='test colour',
            hex_value='000'
        )

    def test_checkout_view(self):
        new_colour = Colour.objects.get(colour='test colour')
        session = self.client.session
        session['basket'] = {new_colour.product.id: 1}
        session.save()
        response = self.client.get(reverse('checkout'), follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    def test_get_empty_basket_for_checkout(self):
        response = self.client.get(reverse('checkout'), follow=True)
        messages = list(get_messages(response.wsgi_request))
        expected_message = "There's nothing in your basket at the moment"

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
        self.assertEqual(messages[0].tags, 'error')
        self.assertEqual(str(messages[0]), expected_message)

    def test_checkout_view_post(self):
        new_colour = Colour.objects.get(colour='test colour')
        session = self.client.session
        session['basket'] = {new_colour.product.id: 1}
        session.save()
        post_data = {
            'full_name': 'Mr test',
            'email': 'test@test.com',
            'phone_number': '123245789',
            'address_1': '1 My Street',
            'address_2': 'My Village',
            'city': 'My City',
            'county': 'My County',
            'country': 'GB',
            'postcode': 'AB12CD',
            'client_secret': 'client_123456_secret_123456',
        }
        response = self.client.post(reverse('checkout'),
                                    data=post_data, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')

    def test_checkout_success_view(self):
        new_product = Product.objects.get(product_name='test product')
        new_colour = Colour.objects.get(colour='test colour')
        new_order = Order.objects.create(
            full_name='Mr test',
            email='test@test.com',
            phone_number='123245789',
            address_1='1 My Street',
            address_2='My Village',
            city='My City',
            county='My County',
            country='GB',
            postcode='AB12CD',
        )
        OrderLineItem.objects.create(
            order=new_order,
            product=new_product,
            colour=new_colour,
            quantity=1)
        response = self.client.get(
            reverse('checkout_success',
                    kwargs={'order_number': new_order.order_number}))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')

    def tearDown(self):
        new_category = Category.objects.get(name='test_category')
        new_product = Product.objects.get(product_name='test product')
        new_colour = Colour.objects.get(colour='test colour')

        del new_category
        del new_product
        del new_colour
