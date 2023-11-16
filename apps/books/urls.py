from django.urls import path
from . import views


urlpatterns = [
    path('publishers/', views.PublishersView.as_view()), # create, get all
    path('publishers/<int:pk>/', views.PublisherDetailView.as_view()), # get, update, delete
    path('languages/', views.LanguagesView.as_view()), # create, get all
    path('languages/<int:pk>/', views.LanguageDetailView.as_view()), # get, update, delete
    path('', views.BooksView.as_view()), # create, get all
    path('<int:pk>/', views.BookDetailView.as_view()), # get, update, delete
    path('authors/', views.AuthorsView.as_view()), # create, get all
    path('authors/<int:pk>/', views.AuthorDetailView.as_view()), # get, update, delete
    path('genres/', views.GenresView.as_view()), # create, get all
    path('genres/<int:pk>/', views.GenreDetailView.as_view()), # get, update, delete
]
