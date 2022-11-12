"""deepclean URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from cleaning import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePage.as_view(), name='home'),
    path('edit_booking/<int:booking_id>', views.EditBooking.as_view(),
         name='edit_booking'),
    path('cancel_booking/<int:booking_id>', views.cancel_booking,
         name='cancel_booking'),
    path('reviews/', views.Review.as_view(), name='reviews'),
    path('edit_review/<int:review_id>', views.EditReview.as_view(),
         name='edit'),
    path('deepcleaning/', views.DeepClean.as_view(), name='deepcleaning'),
    path('generalcleaning/', views.GeneralClean.as_view(),
         name='generalcleaning'),
    path('contactus/', views.ContactUs.as_view(), name='contactus'),
    path('summernote/', include('django_summernote.urls')),
    path('accounts/', include('allauth.urls')),
]
