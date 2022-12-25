from django.urls import path
from . import views

urlpatterns = [
    path('',views.form_page),
    path('register',views.register),
    path('login',views.login),
    path('wall_page',views.wall_page),
    path('add_message',views.add_message),
    path('add_comment',views.add_comment),
]