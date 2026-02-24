from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('home/',views.index),
    path('about/',views.about),
    path('contact/',views.contact),
    path('faqs/',views.faqs),
    path('booknow/',views.booknow),
    path('register/',views.register),
    path('service/',views.service),
    path('login/',views.login),
    path('logout/',views.logout),
    path('profile/',views.profile),
    path('history/',views.bookinghistory),
    path('allservices/',views.allservices),
]