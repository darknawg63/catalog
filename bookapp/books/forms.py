from django import forms
from .models import Publisher

class PublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name', 'address', 'city', 'state_province']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'vTextField',
                    'placeholder': 'Name'
                }
            ),

            'address': forms.TextInput(
                attrs={
                    'class': 'vTextField',
                    'placeholder': "Address"
                }
            ),

            'city': forms.TextInput(
                attrs={
                    'class': 'vTextField',
                    'placeholder': "City"
                }
            ),

            'state_province': forms.TextInput(
                attrs={
                    'class': 'vTextField',
                    'placeholder': "State"
                }
            )

          }
