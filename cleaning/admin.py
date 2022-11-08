from django.contrib import admin
from .models import Reviews, BookingSystem, Questionnaire
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Reviews)
class ReviewAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')


@admin.register(BookingSystem)
class BookingConfirmation(SummernoteModelAdmin):
    summernote_fields = ('self')


@admin.register(Questionnaire)
class Questions(SummernoteModelAdmin):
    summernote_fields = ('question')
