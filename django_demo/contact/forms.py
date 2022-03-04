"""
Here we define all django forms

"""

from django import forms
from .models import Contact

# lets define model form

class ContactModelForm(forms.ModelForm):
    class Meta:
        # model
        model = Contact
        fields = ('name', 'mobile_number', 'date_of_birth', 'email', 'location')

    def clean_email(self):
        # Get the user submitted word from the cleaned_data dictionary
        email = self.cleaned_data["email"]

        domain = email.split('@')[1]
        if domain != 'wipro.com':
            raise forms.ValidationError("Please enter the wipro email ID")
        # Return data even though it was not modified
        return email

    def clean_mobile_number(self):
        # Get the user submitted word from the cleaned_data dictionary
        mobile_number = self.cleaned_data["mobile_number"]
        # validation len shoulb be 10
        char_len = len(mobile_number)
        if char_len < 10:
            raise forms.ValidationError("Please enter valid mobile number")

        if char_len > 10:
            raise forms.ValidationError("Please enter valid mobile number")

        # Return data even though it was not modified
        return mobile_number






