from django.test import TestCase
from django.contrib.messages import get_messages
from django.shortcuts import reverse
from products.models import Product, Category, Colour


class TestBasketViews(TestCase):

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

    def test_view_basket(self):
        response = self.client.get(reverse('view_basket'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'basket/basket.html')

    def test_add_to_basket(self):
        new_product = Product.objects.get(product_name='test product')
        new_colour = Colour.objects.get(colour='test colour')
        post_data = {
            'colour': new_colour.id,
            'quantity': '1',
            'redirect_url': '/'
        }
        response = self.client.post(reverse('add_to_basket', kwargs={'product_id': new_product.id}), data=post_data)
        messages = list(get_messages(response.wsgi_request))
        expected_message = f"Successfully added {post_data['quantity']} x {new_product.product_name} ({new_colour.colour}) to your basket"

        self.assertRedirects(response, '/')
        self.assertEqual(messages[0].tags, 'success')
        self.assertEqual(str(messages[0]), expected_message)

        """
        Test adding additional item
        """

        post_data_2 = {
            'colour': new_colour.id,
            'quantity': '2',
            'redirect_url': '/'
        }
        response_2 = self.client.post(reverse('add_to_basket', kwargs={'product_id': new_product.id}), data=post_data_2)
        messages_2 = list(get_messages(response_2.wsgi_request))
        expected_message_2 = f"Successfully updated {new_product.product_name} ({new_colour.colour}) quantity to {int(post_data_2['quantity'])}"
        
        self.assertRedirects(response_2, '/')
        self.assertEqual(messages_2[0].tags, 'success')
        self.assertEqual(str(messages_2[0]), expected_message_2)

    
    def test_update_basket(self):
        new_product = Product.objects.get(product_name='test product')
        new_colour = Colour.objects.get(colour='test colour')
        post_data = {
            'colour': new_colour.id,
            'quantity': '1',
            'redirect_url': '/'
        }
        self.client.post(reverse('add_to_basket', kwargs={'product_id': new_product.id}), data=post_data)

        """
        Test amending quantity in the basket
        """

        post_data_2 = {
            'quantity': '2',
        }
        response = self.client.post(reverse('update_basket', kwargs={'colour_id': new_colour.id}), data=post_data_2)
        messages = list(get_messages(response.wsgi_request))
        expected_message = f"Successfully updated {new_product.product_name} ({new_colour.colour}) quantity to {int(post_data_2['quantity'])}"

        self.assertRedirects(response, '/basket/')
        self.assertEqual(messages[1].tags, 'success')
        self.assertEqual(str(messages[1]), expected_message)

        """
        Test amending quantity to 0 in the basket
        """

        post_data_3 = {
            'quantity': '0',
        }
        response_2 = self.client.post(reverse('update_basket', kwargs={'colour_id': new_colour.id}), data=post_data_3)
        messages_2 = list(get_messages(response_2.wsgi_request))
        expected_message_2 = f"Successfully removed {new_product.product_name} ({new_colour.colour}) from your basket"

        self.assertRedirects(response_2, '/basket/')
        self.assertEqual(messages_2[0].tags, 'success')
        self.assertEqual(str(messages_2[0]), expected_message_2)


    def test_remove_from_basket(self):
        new_product = Product.objects.get(product_name='test product')
        new_colour = Colour.objects.get(colour='test colour')
        post_data = {
            'colour': new_colour.id,
            'quantity': '1',
            'redirect_url': '/'
        }
        self.client.post(reverse('add_to_basket', kwargs={'product_id': new_product.id}), data=post_data)
        response = self.client.post(reverse('remove_from_basket', kwargs={'colour_id': new_colour.id}))
        messages = list(get_messages(response.wsgi_request))
        expected_message = f"Successfully removed {new_product.product_name} ({new_colour.colour}) from your basket"

        self.assertRedirects(response, '/basket/')
        self.assertEqual(messages[1].tags, 'success')
        self.assertEqual(str(messages[1]), expected_message)

    def tearDown(self):
        new_category = Category.objects.get(name='test_category')
        new_product = Product.objects.get(product_name='test product')
        new_colour = Colour.objects.get(colour='test colour')

        del new_category
        del new_product
        del new_colour
