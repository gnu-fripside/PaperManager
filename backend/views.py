from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .utils import util
from .models import Book, Users
import json


# Create your views here.
# @require_http_methods(["GET"])
def add_book(request):
    response = {}
    try:
        book = Book(book_name=request.GET.get('book_name'))
        book.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)


# @require_http_methods(["GET"])
def show_books(request):
    response = {}
    try:
        books = Book.objects.filter()
        response['list'] = json.loads(serializers.serialize("json", books))
        response['msg'] = 'success'
        response['error_num'] = 0
    except Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response)

def getTagList(request):
    userId = request.GET.get('userId')
    currentPath = request.GET.get('currentPath')
    response = util.getTagList(userId, currentPath)
    return JsonResponse(response)

def getFileList(request):
    userId = request.GET.get('userId')
    currentPath = request.GET.get('currentPath')
    response = util.getFileList(userId, currentPath)
    return JsonResponse(response)

# @require_http_methods(["GET"])
def register(request):
    response = {"error_num": 0}
    user_name = request.GET.get('userId')
    user_password = request.GET.get('password')
    if len(Users.objects.filter(user_name=user_name)) > 0:
        response["error_num"] += 1
        response["msg"] = "The user has been registered!"
    else:
        user = Users.objects.create(user_name=user_name, user_password=user_password)
        user.save()
    return JsonResponse(response)

def login(request):
    response = {"error_num": 0}
    user_name = request.GET.get('userId')
    user_password = request.GET.get('password')
    try:
        user = Users.objects.get(user_name=user_name).__dict__
        if user_password != user['user_password']:
            response["error_num"] += 1
            response["msg"] = "The password is wrong!"
    except Exception as e:
        response["msg"] = str(e)
        response["error_num"] += 1
    res = JsonResponse(response)
    if response['error_num'] == 0:
        res.set_cookie('user_name', user_name, 360001)
    return res

