from django.http import JsonResponse
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from .utils import util
from .models import *
import json


def user_register(request):
    """
    User register
    :param request: request
    :return: response{"error_num", "msg":message of error}
    """
    response = {}
    username = request.POST['username']
    password = request.POST['password']
    email = request.POST['email']
    if Users.objects.filter(username=username):
        response['error_num'] = 1
        response['msg'] = 'The user has been registered!'
    else:
        user = Users.objects.create(username=username, password=password, email=email)
        user.save()
        response['error_num'] = 0
        response['msg'] = 'success'
    return JsonResponse(response)


def user_login(request):
    """
    User login
    :param request: request
    :return: response{"error_num", "msg":message of errors}
    """
    response = {}
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            response['error_num'] = 0
            response['msg'] = "success"
        else:
            response['error_num'] = 1
            response['msg'] = "user is frozen"
    else:
        response['error_num'] = 1
        response['msg'] = "user does not exist or is frozen"
    res = JsonResponse(response)
    if response['error_num'] == 0:
        res.set_cookie('username', username, 360001)
    return res


def user_logout(request):
    """
    User logout
    :param request: request
    :return: logout success Json Response
    """
    logout(request)
    response = {'error_num': 0, 'msg': 'logout success'}
    res = JsonResponse(response)
    return res


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
