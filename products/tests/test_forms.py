from django.test import TestCase
from products.forms import ProductForm, ColourForm


class TestProductForm(TestCase):

    def test_product_form_required_fields(self):
        form = ProductForm({
                            'brand_name': '',
                            'product_name': '',
                            'price': '',
                            'description': ''
                        })

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['brand_name'][0], 'This field is required.')
        self.assertEqual(
            form.errors['product_name'][0], 'This field is required.')
        self.assertEqual(
            form.errors['price'][0], 'This field is required.')
        self.assertEqual(
            form.errors['description'][0], 'This field is required.')

    def test_product_form_minimum_required_data_is_valid(self):
        form = ProductForm({
                            'brand_name': 'test_brand',
                            'product_name': 'test product',
                            'price': '1',
                            'description': 'test description'
                        })

        self.assertTrue(form.is_valid())

    def test_product_form_slug_field_excluded(self):
        form = ProductForm()
        self.assertEqual(form.Meta.exclude, ('slug',))


class TestColourForm(TestCase):

    def test_colour_form_required_fields(self):
        form = ColourForm({'colour': '', 'hex_value': ''})

        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['colour'][0], 'This field is required.')
        self.assertEqual(
            form.errors['hex_value'][0], 'This field is required.')
