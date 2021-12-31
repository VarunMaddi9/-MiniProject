from django.contrib import admin
from django.urls import path
from . import views

urlpatterns=[
    path('login/',views.loginview,name='login'),
    path('logout/',views.logoutview,name='logout'),
    path('contactus/',views.contactusview,name="contactus"),
    path('signup/',views.signupview,name='signup'),
    path('seller/',views.sellerview,name="seller"),
    path('bidder/',views.bidderview,name="bidder"),
    path('select/',views.selectview,name="select"),
    path('announcement/',views.announcementview,name="announcements"),
    path('bidding/<objectid>',views.biddingview,name="bidding"),
]
