from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic, View
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.core.exceptions import MultipleObjectsReturned
from .models import Reviews
from .forms import ReviewForm


class HomePage(generic.TemplateView):
    template_name = "index.html"


class Review(generic.FormView):
    review_form = ReviewForm
    form_class = ReviewForm
    template_name = "reviews.html"

    def get(self, request, *args, **kwargs):
        queryset = Reviews.objects.filter(status=1).order_by("-created")
        
        self.reviews = queryset
        self.form = self.get_form(self.form_class)
        context = {
            "reviews": self.reviews,
            "reviews_form": ReviewForm()
        }
        return generic.FormView.get(self, request, context)
    
    def post(self, request, *args, **kwargs):
        queryset = Reviews.objects.filter(status=1)
        review = queryset
        review_form = ReviewForm(data=request.POST)
        context = {"review_form": review_form}
        if review_form.is_valid():
            review_form.instance.name = request.user
        
            review_form.review = review

            review_form.save()
        else:
            review_form = ReviewForm()
        return HttpResponseRedirect(reverse("reviews"))

    def get_context_data(self, **kwargs):
        context = super(Review, self).get_context_data(**kwargs)
        context['form'] = ReviewForm
        context['reviews'] = self.reviews
        return context
