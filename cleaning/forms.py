from .models import Reviews, BookingSystem
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['title', 'content', 'image', ]


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingSystem
        fields = ['cleaning_type', 'cleaning_date', 'time_slot']
