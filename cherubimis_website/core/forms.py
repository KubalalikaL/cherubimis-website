from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = [
            'first_name',
            'last_name',
            'business_email',
            'company_name',
            'state_region',
            'country_region',
            'inquiry',
        ]

        labels = {
            'first_name': 'Your First Name',
            'last_name': 'Your Last Name',
            'business_email': 'Your Business Email Address',
            'company_name': 'Your Company Name',
            'state_region': 'State or Region',
            'country_region': 'Country or Region',
            'inquiry': 'Please add your Question or Inquiry in the space below',
        }

        widgets = {
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'business_email': forms.EmailInput(attrs={'placeholder': 'Business Email'}),
            'company_name': forms.TextInput(attrs={'placeholder': 'Company Name'}),
            'state_region': forms.TextInput(attrs={'placeholder': 'State/Region', }),
            'country_region': forms.TextInput(attrs={'placeholder': 'Country/Region'}),
            'inquiry': forms.Textarea(attrs={'rows': 5}),
        }
