from django import forms
from .models import Contact

# A form that maps to the Contact model
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
