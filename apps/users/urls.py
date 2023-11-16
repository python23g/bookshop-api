from django.urls import path
from . import views


urlpatterns = [
    path('', views.UsersView.as_view()), # create, get all
    path('<int:pk>/', views.UserDetailView.as_view()), # get, update, delete
    path('<int:pk>/profile/', views.ProfileView.as_view()), # create, get all
]
