from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic, View
from django.views.generic import FormView, TemplateView
from django.http import HttpResponseRedirect
from django.core.exceptions import MultipleObjectsReturned
from .models import Reviews, BookingSystem, Questionnaire
from .forms import ReviewForm, BookingForm, QuestionForm


class HomePage(FormView):
    booking_form = BookingForm
    form_class = BookingForm
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        self.booking_pending = BookingSystem.objects.filter(status=0)
        self.booking_approved = BookingSystem.objects.filter(status=1)
        self.form = self.get_form(self.form_class)
        context = {"booking_form": self.form_class,
                   "booking_pending": self.booking_pending,
                   "booking_approved": self.booking_approved}
        return FormView.get(self, request, context)

    def post(self, request, *args, **kwargs):
        booking_form = BookingForm(data=request.POST)
        context = {"booking_form": booking_form}
        if booking_form.is_valid():
            booking_form.instance.name = request.user
            booking_form.save()
        else:
            booking_form = BookingForm()
        return HttpResponseRedirect(reverse("deepcleaning"))

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['booking_form'] = BookingForm
        context['booking_pending'] = self.booking_pending
        context['booking_approved'] = self.booking_approved
        return context


class Review(FormView):
    review_form = ReviewForm
    form_class = ReviewForm
    template_name = "reviews.html"

    def get(self, request, *args, **kwargs):
        self.reviews = Reviews.objects.filter(status=1).order_by("-created")
        self.form = self.get_form(self.form_class)
        context = {
            "reviews": self.reviews,
            "reviews_form": ReviewForm()
        }
        return FormView.get(self, request, context)

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
        context['review_form'] = ReviewForm
        context['reviews'] = self.reviews
        return context


class DeepClean(TemplateView):
    template_name = 'deepcleaning.html'


class GeneralClean(TemplateView):
    template_name = 'generalcleaning.html'


class ContactUs(FormView):
    form_class = QuestionForm
    template_name = "contactus.html"

    def get(self, request, *args, **kwargs):
        self.questions = Questionnaire.objects.filter(status=0)
        self.question_form = self.get_form(self.form_class)
        context = {
            'questions': self.questions,
            'question_form': self.form_class
        }
        return FormView.get(self, request, context)

    def post(self, request, *args, **kwargs):
        questions = Questionnaire.objects.filter(status=0)
        question_form = QuestionForm(data=request.POST)
        context = {"question_form": question_form}
        if question_form.is_valid():
            question_form.instance.name = request.user
            question_form.questions = questions
            question_form.save()
        else:
            question_form = QuestionForm()
        return HttpResponseRedirect(reverse("contactus"))

    def get_context_data(self, **kwargs):
        context = super(ContactUs, self).get_context_data(**kwargs)
        context['question_form'] = QuestionForm
        context['questions'] = self.questions
        return context
