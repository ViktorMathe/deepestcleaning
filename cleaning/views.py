from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Reviews
from .forms import ReviewForm


class HomePage(generic.TemplateView):
    template_name = "index.html"


class Review(generic.ListView):
    model = Reviews
    queryset = Reviews.objects.filter(status=1).order_by('-created')
    template_name = "reviews.html"
    
    def post(self, request, slug, *args, **kwargs):
        queryset = Reviews.objects.all()
        reviews = get_object_or_404(queryset, slug=slug)
        add_review = ReviewForm(data=request.POST)
        if add_review.is_valid():
            review.save()
        else:
            add_review = ReviewForm()
        
        context = {
                "add_review": add_review
            }

        return render(request, "reviews.html", context)
