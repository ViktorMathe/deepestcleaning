from .models import Reviews, BookingSystem
from django import forms


class DateInput(forms.DateInput):
    input_type = "date"


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['title', 'content', 'image', ]


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingSystem
        fields = ['cleaning_type', 'cleaning_date', 'time_slot']
        widgets = {
            "cleaning_date": DateInput()
        }
