from django.core.handlers.wsgi import WSGIRequest
from django.http.response import JsonResponse


def user_list(request: WSGIRequest) -> JsonResponse:
    """ ユーザー一覧を表示する """
    return JsonResponse({})


def user_create(request: WSGIRequest) -> JsonResponse:
    """ 新規にユーザーを作る """
    return JsonResponse({})
