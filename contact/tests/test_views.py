from django.test import TestCase
from django.urls import reverse
from django.contrib.messages import get_messages
from contact.models import Subscription, SecureMessage
from contact.forms import SubscriptionForm, SecureMessageForm

class TestContactViews(TestCase):

    def setUp(self):

        new_secure_message = SecureMessage.objects.create(
            name='Mr Test', 
            email='test@test.com', 
            message='test secure message'
        )

    def test_new_subscription_email_and_redirect(self):
        response = self.client.post(reverse('subscribe'), data={'email': 'test@test.com', 'subscribe_redirect': '/'})
        messages = list(get_messages(response.wsgi_request))
        expected_message = 'You are now subscribed to our newsletter.'

        self.assertRedirects(response, '/')
        self.assertEqual(str(messages[0]), expected_message)

    def test_existing_subscription_email_and_redirect(self):
        new_subscription = Subscription.objects.create(
            email='test@test.com'
        )
        response = self.client.post(reverse('subscribe'), data={'email': 'test@test.com', 'subscribe_redirect': '/'})
        messages = list(get_messages(response.wsgi_request))
        expected_message = 'You are aleady subscribed to our newsletter.'

        self.assertRedirects(response, '/')
        self.assertEqual(str(messages[0]), expected_message)

    def tearDown(self):
        new_secure_message = SecureMessage.objects.get(name='Mr Test')

        del new_secure_message