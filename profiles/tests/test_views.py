from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import UserProfile


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
        self.assertRedirects(response, "/accounts/login/?next=/profile/")

    def tearDown(self):
            new_user = UserProfile.objects.get(user__username='test_user')

            del new_user