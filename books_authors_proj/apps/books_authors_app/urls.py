from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^authors$', views.authors),
    url(r'^books/(?P<book_id>\d+)$', views.view_book),
    url(r'^books/edit/(?P<book_id>\d+)$', views.edit_book),
    url(r'^books/delete/(?P<book_id>\d+)$', views.delete_book),
    url(r'^edit_book$', views.update_book),
    url(r'^authors/(?P<author_id>\d+)$', views.view_author),
    url(r'^create_book$', views.add_book),
    url(r'^add_author_to_book$', views.add_author_to_book),
]
