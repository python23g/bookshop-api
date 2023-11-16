from django.views import View
from django.http import HttpRequest, JsonResponse
from .models import Publisher, Language, Book, Author, Genre
from django.forms import model_to_dict
import json
from django.core.exceptions import ObjectDoesNotExist


class PublishersView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        pass
    
    def post(self, request: HttpRequest) -> JsonResponse:
        pass
    

class PublisherDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    
    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    
    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass


class LanguagesView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        pass
    
    def post(self, request: HttpRequest) -> JsonResponse:
        pass
    

class LanguageDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    
    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    
    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass


class BooksView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        params = request.GET

        if params.get('title', False):
            books = Book.objects.filter(title__icontains=params.get('title'))
        elif params.get('description', False):
            books = Book.objects.filter(description__icontains=params.get('description'))
        elif params.get('price', False):
            books = Book.objects.filter(price__lte=params.get('price'))
        elif params.get('lang', False):
            books = Book.objects.filter(lang__lang__icontains=params.get('lang'))
        elif params.get('publisher', False):
            books = Book.objects.filter(publisher__name__icontains=params.get('publisher'))
        else:
            books = Book.objects.all()

        result = [model_to_dict(book) for book in books]
        return JsonResponse(result, safe=False)
         
    def post(self, request: HttpRequest) -> JsonResponse:
        pass
    

class BookDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    
    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    
    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass


class AuthorsView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        params = request.GET

        if params.get('title', False):
            books = Book.objects.filter(title__icontains=params.get('title'))
        elif params.get('description', False):
            books = Book.objects.filter(description__icontains=params.get('description'))
        elif params.get('price', False):
            books = Book.objects.filter(price__lte=params.get('price'))
        elif params.get('lang', False):
            books = Book.objects.filter(lang__lang__icontains=params.get('lang'))
        elif params.get('publisher', False):
            books = Book.objects.filter(publisher__name__icontains=params.get('publisher'))
        else:
            books = Book.objects.all()

        result = [model_to_dict(book) for book in books]
        return JsonResponse(result, safe=False)
         
    def post(self, request: HttpRequest) -> JsonResponse:
        pass
    

class AuthorDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    
    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    
    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    


class GenresView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        params = request.GET

        if params.get('title', False):
            books = Book.objects.filter(title__icontains=params.get('title'))
        elif params.get('description', False):
            books = Book.objects.filter(description__icontains=params.get('description'))
        elif params.get('price', False):
            books = Book.objects.filter(price__lte=params.get('price'))
        elif params.get('lang', False):
            books = Book.objects.filter(lang__lang__icontains=params.get('lang'))
        elif params.get('publisher', False):
            books = Book.objects.filter(publisher__name__icontains=params.get('publisher'))
        else:
            books = Book.objects.all()

        result = [model_to_dict(book) for book in books]
        return JsonResponse(result, safe=False)
         
    def post(self, request: HttpRequest) -> JsonResponse:
        pass
    

class GenreDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    
    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    
    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    