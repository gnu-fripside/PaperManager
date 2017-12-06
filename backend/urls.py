from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^register$', views.user_register),
    url(r'^login$', views.user_login),
]
