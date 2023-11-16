from django.contrib import admin
from .models import Publisher, Language, Book, Author, Genre

all_models = (Publisher, Language, Book, Author, Genre)

admin.site.register(all_models)