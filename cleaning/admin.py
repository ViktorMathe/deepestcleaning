from django.contrib import admin
from .models import Reviews
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.


@admin.register(Reviews)
class ReviewAdmin(SummernoteModelAdmin):
    summernote_fields = ('content')
