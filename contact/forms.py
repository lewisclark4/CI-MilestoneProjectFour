from django import forms
from .models import Subscription, SecureMessage


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ["email_address"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            "email_address": "Email Address",
        }

        for field in self.fields:
            placeholder = placeholders[field]
            self.fields[field].widget.attrs["placeholder"] = placeholder
            self.fields[field].label = False

class SecureMessageForm(forms.ModelForm):
    class Meta:
        model = SecureMessage
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
            