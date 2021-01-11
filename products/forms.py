from django import forms
from .models import Product, Category, Colour


class ProductForm(forms.ModelForm):
    """
    This form will display all model fields
    except slug as this is updated on save.
    It will display category friendly names
    for improved user experience
    """
    class Meta:
        model = Product
        exclude = ('slug',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names


class ColourForm(forms.ModelForm):

    class Meta:
        model = Colour
        fields = '__all__'
