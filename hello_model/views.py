from django.core.handlers.wsgi import WSGIRequest
from django.http.response import JsonResponse

from .models import User


def user_list(request: WSGIRequest) -> JsonResponse:
    """ ユーザー一覧を表示する """
    users = User.objects.all()
    user_list = [{"id": user.id, "name": user.name} for user in users]

    return JsonResponse({"user_list": user_list})


def user_create(request: WSGIRequest, user_id: int) -> JsonResponse:
    """ 新規にユーザーを作る """
    name = request.GET.get("name") or "No Name"
    user = User(id=user_id, name=name)
    user.save()

    return JsonResponse({"id": user.id, "name": user.name})
