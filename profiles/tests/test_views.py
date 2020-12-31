from django.test import TestCase
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from profiles.models import UserProfile
from profiles.forms import UserProfileForm


class TestProfilesViews(TestCase):
    def setUp(self):
            new_user = User.objects.create_user(
                username='test_user', password='verysecretpassword1!'
            )

    def test_profile_view(self):
        self.client.login(username='test_user', password='verysecretpassword1!')
        response = self.client.get('/profile/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')

    def test_profile_view_not_logged_in(self):
        response = self.client.get('/profile/')

        self.assertRedirects(response, '/accounts/login/?next=/profile/')

    def test_update_profile_form(self):
        self.client.login(username='test_user', password='verysecretpassword1!')
        data = {"default_phone_number": "12345"}
        response = self.client.post("/profile/", data)
        messages = list(get_messages(response.wsgi_request))
        expected_message = 'Your delivery details were updated successfully'

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
        self.assertEqual(messages[0].tags, "success")
        self.assertEqual(str(messages[0]), expected_message)

    def test_order_history_view(self):
        self.client.login(username='test_user', password='verysecretpassword1!')
        response = self.client.get('/profile/order_history/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/order_history.html')
    
    def test_order_history_view_not_logged_in(self):
        response = self.client.get('/profile/order_history/')

        self.assertRedirects(response, '/accounts/login/?next=/profile/order_history/')

    def tearDown(self):
            new_user = UserProfile.objects.get(user__username='test_user')

            del new_user