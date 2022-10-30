from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Reviews
from django.http import HttpResponseRedirect
from .forms import ReviewForm


def home(request):
    return render(request, '../templates/index.html')


def review(request):
    reviews = Reviews.objects.all()
    context = {
        'reviews': reviews
    }
    return render(request, '../templates/review.html', context)


def add_review(self, request, slug, *args, **kwards):
    review_form = ReviewForm(data=request.POST)
    if review_form.is_valid():
        review_form.instance.title = request.title
        review = review_form.save(commit=False)
        review.count()
        review.save()
