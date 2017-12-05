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
        root = ClassificationTree.objects.create(name='root')
        user = Users.objects.create(username=username, password=password, email=email, classification_tree_root=root)
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


def add_classification(request):
    """
    add node in the classification tree
    :param request: request
    :return: Json response{'error_num', 'msg': message of the error}
    """
    response = {}
    father_name = request.POST['father_name']
    new_name = request.POST['name']
    father = ClassificationTree.objects.filter(name=father_name)
    exist = ClassificationTree.objects.filter(name=new_name)
    if father is None:
        response['error_num'] = 1
        response['msg'] = 'the father node does not exist'
    elif exist is not None:
        response['error_num'] = 2
        response['msg'] = 'the node name had existed'
    else:
        node = ClassificationTree.objects.create(father[0], new_name)
        response['error_num'] = 0
        response['msg'] = 'success'
    res = JsonResponse(response)
    return res


def add_paper(request):
    """
    add paper in one node of the classification tre
    :param request: request
    :return: later add
    """
    response = {}
    title = request.POST['title']
    author = request.POST['author']
    publish_time = request.POST['publish_time']
    add_time = request.POST['add_time']
    source = request.POST['source']
    url = request.POST['url']
    hash_code = request.POST['hash_code']
    node_name = request.POST['node_name']
    node = ClassificationTree.objects.filter(name=node_name)
    paper = Paper.objects.create(title=title, publish_time=publish_time,
                                 add_time=add_time, source=source,
                                 url=url, hash_code=hash_code,
                                 classification_tree_node=node[0])
    for au in author:
        paper.author.add(au)
    response['error_num'] = 0
    response['msg'] = 'success'
    res = JsonResponse(response)
    return res


def save_node(request):
    """
    add and change node for a paper
    :param request: request
    :return: later add
    """
    response = {}
    paper_title = request['paper_title']
    paper = Paper.objects.filter(title=paper_title)
    paper_page = request['paper_page']
    if Note.objects.filter(paper_title=paper_title, paper_page=paper_page):
        Note[0].delete()
        response['msg'] = 'change note successfully'
    else:
        response['msg'] = 'add note successfully'
    note = Note.objects.create(paper_title, paper_page, paper[0])
    response['error_num'] = 0
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
