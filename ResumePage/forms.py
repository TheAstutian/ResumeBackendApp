from django.forms import ModelForm, Textarea
from .models import Contact

class ContactForm(ModelForm):
    class Meta: 
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            "message": Textarea(
                attrs={
                    "placeholder": "Enter a message"
                }
            )
        }