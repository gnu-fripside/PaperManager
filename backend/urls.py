from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^register$', views.user_register),
    url(r'^login$', views.user_login),
    url(r'^add_classification$', views.add_classification),
    url(r'^add_paper$', views.add_paper),
    url(r'^update_paper_info$', views.update_paper_info),
    url(r'^update_read_status$', views.update_read_status),
    url(r'^save_note$', views.save_note),
    url(r'^show_paper_detail$', views.show_paper_detail),
    url(r'^show_paper$', views.read_paper),
    url(r'^show_paper_of_the_node$', views.show_paper_of_the_node),
    url(r'^show_classification_tree$', views.show_classification_tree),
    url(r'^SubTreePaperPack$', views.SubTreePaperPack),
    url(r'^paper_node_pack$', views.paper_node_pack),
]
