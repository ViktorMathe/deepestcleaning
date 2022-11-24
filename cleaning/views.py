from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.views import generic, View
from django.views.generic import FormView, TemplateView
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Reviews, BookingSystem
from .forms import ReviewForm, BookingForm
from cloudinary.forms import cl_init_js_callbacks
import datetime


class HomePage(FormView):
    booking_form = BookingForm()
    form_class = BookingForm
    template_name = "index.html"

    def get(self, request, *args, **kwargs):
        self.booking_pending = BookingSystem.objects.filter(status=0)
        self.booking_approved = BookingSystem.objects.filter(status=1)
        self.form = self.get_form(self.form_class)
        context = {"booking_pending": self.booking_pending,
                   "booking_approved": self.booking_approved}
        return FormView.get(self, request, context)

    def post(self, request, *args, **kwargs):
        booking_form = BookingForm(data=request.POST)
        context = {"booking_form": booking_form}
        success_message = messages.add_message(
            request,
            messages.SUCCESS,
            """Booking was successfull! You can view it now
             in the Pending Booking secition!""")
        if booking_form.is_valid():
            booking_form.instance.name = request.user
            booking_form.save()
            return HttpResponseRedirect(reverse("home"), success_message)
        else:
            return render(request, 'index.html', {'form': booking_form})

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['booking_form'] = BookingForm()
        context['booking_pending'] = self.booking_pending
        context['booking_approved'] = self.booking_approved
        return context


class EditBooking(View):

    def get(self, request, booking_id):
        booking = get_object_or_404(BookingSystem, id=booking_id)
        booking_form = BookingForm(instance=booking)
        context = {
            'booking': booking,
            'booking_form': booking_form,
            }
        return render(request, 'edit_booking.html', context)

    def post(self, request, booking_id):
        booking = get_object_or_404(BookingSystem, id=booking_id)
        booking_form = BookingForm(request.POST, instance=booking)
        edit_booking_msg = messages.add_message(
            request,
            messages.INFO,
            "Your Booking has been edited!")
        if booking_form.is_valid():
            booking_form.instance.name = request.user
            booking_form.save()
        context = {
            'booking': booking,
            'booking_form': booking_form,
            }
        return HttpResponseRedirect(reverse('home'), context, edit_booking_msg)


def approve_booking(request, booking_id):
    approve_msg = messages.add_message(
        request,
        messages.SUCCESS,
        "Booking has been approved!")
    approve_booking = get_object_or_404(BookingSystem, id=booking_id)
    approve_booking.status = not approve_booking.status
    approve_booking.save()
    return HttpResponseRedirect(reverse('home'), approve_msg)


@login_required
def cancel_booking(request, booking_id):
    cancel_msg = messages.add_message(
        request,
        messages.ERROR,
        "Booking has been deleted!")
    cancel_booking = BookingSystem.objects.filter(id=booking_id)
    cancel_booking.delete()
    return redirect('home')


class Review(FormView):
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
        review_form = ReviewForm(request.POST, request.FILES)
        add_review_msg = messages.add_message(
            request,
            messages.SUCCESS,
            "You succesfully left a review!")
        context = {"review_form": review_form}
        if review_form.is_valid():
            review_form.instance.name = request.user
            review_form.save()
        else:
            review_form = ReviewForm()
        return HttpResponseRedirect(reverse("reviews"), add_review_msg)

    def get_context_data(self, **kwargs):
        context = super(Review, self).get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        context['reviews'] = self.reviews
        return context


class EditReview(View):

    def get(self, request, review_id):
        edit = get_object_or_404(Reviews, id=review_id)
        edit_form = ReviewForm(instance=edit)
        context = {
                'edit': edit,
                'edit_form': edit_form
                }
        return render(request, 'edit_review.html', context)

    def post(self, request, review_id):
        edit_review_msg = messages.add_message(
            request,
            messages.INFO,
            "Your review has been edited!")
        edit = get_object_or_404(Reviews, id=review_id)
        edit_form = ReviewForm(request.POST, request.FILES, instance=edit)
        if edit_form.is_valid():
            edit_form.instance.name = request.user
            edit_form.save()
        context = {'edit_form': edit_form}
        return HttpResponseRedirect(
            reverse('reviews'),
            context,
            edit_review_msg)


@login_required
def delete_review(request, review_id):
    delete_msg = messages.add_message(
        request,
        messages.ERROR,
        "Review has been deleted!")
    delete_review = Reviews.objects.filter(id=review_id)
    delete_review.delete()
    return redirect('reviews')


class DeepClean(TemplateView):
    template_name = 'deepcleaning.html'


class GeneralClean(TemplateView):
    template_name = 'generalcleaning.html'


class ContactUs(TemplateView):
    template_name = "contactus.html"
