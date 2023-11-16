from django.views import View
from django.http import HttpRequest, JsonResponse
from .models import User, UserProfile
from django.forms import model_to_dict
import json
from django.core.exceptions import ObjectDoesNotExist


class UsersView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        users = User.objects.filter(is_staff=False, is_active=True, is_superuser=False)

        result = [model_to_dict(user) for user in users]
        return JsonResponse(result, safe=False)
    
    def post(self, request: HttpRequest) -> JsonResponse:
        data = json.loads(request.body.decode())

        user = User(username=data.get('username'))
        user.set_password(data.get('password'))
        user.save()

        return JsonResponse(model_to_dict(user), status=201)
    

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
