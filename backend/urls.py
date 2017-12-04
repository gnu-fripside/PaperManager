from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^add_book$', views.add_book,),
    url(r'^show_books$', views.show_books,),
    url(r'^getTagList$', views.getTagList),
    url(r'^getFileList$', views.getFileList),
]
