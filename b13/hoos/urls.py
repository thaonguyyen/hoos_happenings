from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", views.home, name='home'),
    path("logout/", views.logout_view, name='logout'),
    path("hoos_login/", views.admin_login, name='authenticate'),

    path('welcome/', views.welcome, name='welcome'),
    path('listings/', views.listings, name='listings'),
    path('map/', views.map_view, name='map'),
    path('submit_event/', views.submit_event, name='submit_event'),
    path('review_events/', views.review_events, name='review_events'),
    path('approve_event/<int:event_id>/', views.approve_event, name='approve_event'),
    path('reject_event/<int:event_id>/', views.reject_event, name='reject_event'),
    path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
    path('my_events/', views.my_events, name='my_events'),
    path('event_details/<int:event_id>/', views.event_details, name='event_details'),
]
