from django.urls import path
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("", views.home, name='home'),
    path("logout/", views.logout_view, name='logout'),
    path("hoos_login/", views.admin_login, name='authenticate'),

    path("hoos_admin/", views.admin_view, name='home_admin'),
    path("hoos_admin/logout/", views.logout_view, name='admin_logout'),
    path("hoos_admin/map/", views.admin_map, name='admin_map'),
    path("hoos_admin/admin_home/", views.admin_view, name='admin_home'),
    path("hoos_admin/admin_map/", views.admin_map, name='admin_map'),
    path("hoos_admin/review_event/", views.review_events, name='review_event'),
    path('hoos_admin/approve_event/<int:event_id>/', views.approve_event, name='approve_event'),
    path('hoos_admin/admin_event_listings/', views.admin_event_listings, name='admin_event_listings'),
    path('hoos_admin/admin_home/logout/', views.logout_view, name='admin_home_logout'),

    path("hoos_user/", views.user_view, name='home_user'),
    path("hoos_user/submit_event/", views.submit_event, name='submit_event'),
    path("hoos_user/logout/", views.logout_view, name='user_logout'),
    path('hoos_user/user_home/logout/', views.logout_view, name='user_home_logout'),
    path("hoos_user/user_home/", views.user_view, name='user_home'),
    path("hoos_user/user_map/", views.user_map, name='user_map'),
    path('hoos_user/user_event_listings/', views.user_event_listings, name='user_event_listings'),

    path('welcome/', views.welcome, name='welcome')
]