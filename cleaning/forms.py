from .models import Reviews, BookingSystem, Questionnaire
from django import forms


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Reviews
        fields = ['title', 'content', 'image', ]


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingSystem
        fields = ['cleaning_type', 'cleaning_date', 'time_slot']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = ['question']
