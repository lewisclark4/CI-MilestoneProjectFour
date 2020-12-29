from django import forms
from .models import Subscription, Contact


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ["email"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "email": "Email Address",
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].label = False

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "name": "Name",
            "email": "Email Address",
            "message": "Message",
        }

        self.fields["name"].widget.attrs["autofocus"] = True
        for field in self.fields:
            placeholder = f"{placeholders[field]} *"
            self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].label = False
            