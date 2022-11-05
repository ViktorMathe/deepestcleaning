from .models import Reviews
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['title', 'content', 'image', ]
