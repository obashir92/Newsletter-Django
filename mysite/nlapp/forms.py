from django import forms
from .models import Subscriber

class SubscriberForm(forms.ModelForm):
    email = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Your email',
            'class': 'text-black caret-black w-1/2 py-2 px-3 rounded-xl',
        })
    )

    class Meta:
        model = Subscriber
        fields = ['email']
