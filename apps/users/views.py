from django.views import View
from django.http import HttpRequest, JsonResponse
from .models import User, UserProfile
from django.forms import model_to_dict
import json
from django.core.exceptions import ObjectDoesNotExist


class UsersView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        pass
    
    def post(self, request: HttpRequest) -> JsonResponse:
        pass
    

class UserDetailView(View):
    def get(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    
    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    
    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass


class ProfileView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        pass
    
    def post(self, request: HttpRequest) -> JsonResponse:
        pass

    def put(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
    
    def delete(self, request: HttpRequest, pk: int) -> JsonResponse:
        pass
