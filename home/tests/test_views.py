from django.test import TestCase


class TestHomeViews(TestCase):
    def test_base_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
