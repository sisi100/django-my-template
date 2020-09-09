from django.core.handlers.wsgi import WSGIRequest
from django.http.response import JsonResponse

from .models import User


def user_list(request: WSGIRequest) -> JsonResponse:
    """ ユーザー一覧を表示する """
    users = User.objects.all()
    user_list = [
        {"id": user.id, "name": user.name, "age": user.age} for user in users
    ]

    return JsonResponse({"user_list": user_list})


def user_create(request: WSGIRequest, user_id: int) -> JsonResponse:
    """ 新規にユーザーを作る """
    name = request.GET.get("name") or "No Name"
    age = request.GET.get("age") or "20"
    user = User(id=user_id, name=name, age=age)
    user.save()

    return JsonResponse({"id": user.id, "name": user.name, "age": user.age})


def user_update(request: WSGIRequest, user_id: int) -> JsonResponse:
    """ ユーザー情報を更新する """
    user = User.objects.get(id=user_id)
    if name := request.GET.get("name"):
        user.name = name
    if age := request.GET.get("age"):
        user.age = age
    user.full_clean()
    user.save()

    return JsonResponse({})


def user_delete(request: WSGIRequest, user_id: int) -> JsonResponse:
    """ ユーザーを削除する """
    user = User.objects.get(id=user_id)
    user.delete()
    return JsonResponse({})
