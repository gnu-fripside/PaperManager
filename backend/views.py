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
    username = request.POST['username']
    father_name = request.POST['father_name']
    new_name = request.POST['name']
    father = ClassificationTree.objects.filter(name=father_name, username=username)
    exist = ClassificationTree.objects.filter(name=new_name, username=username)
    if father is None:
        response['error_num'] = 1
        response['msg'] = 'the father node does not exist'
    elif exist is not None:
        response['error_num'] = 2
        response['msg'] = 'the node name had existed'
    else:
        node = ClassificationTree.objects.create(username=username,
                                                 ClassificationTree=father[0],
                                                 name=new_name)
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
    username = request.POST['username']
    title = request.POST['title']
    authors = request.POST['author']
    publish_time = request.POST['publish_time']
    add_time = request.POST['add_time']
    source = request.POST['source']
    url = request.POST['url']
    hash_code = request.POST['hash_code']
    node_name = request.POST['node_name']
    node = ClassificationTree.objects.filter(username=username, name=node_name)
    paper = Paper.objects.create(username=username, title=title,
                                 publish_time=publish_time,
                                 add_time=add_time, source=source,
                                 url=url, hash_code=hash_code,
                                 classification_tree_node=node[0])
    for au in authors:
        author = Author.objects.filter(first_name=au['first_name'],
                                       last_name=au['last_name'],
                                       email=au['email'])
        if author:
            paper.author.add(author[0])
        else:
            new_author = Author.objects.create(first_name=au['first_name'], last_name=au['last_name'],
                                               email=au['email'])
            paper.author.add(new_author)
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
    username = request.POST['username']
    paper_title = request.POST['paper_title']
    paper_page = request.POST['paper_page']
    exist = Note.objects.filter(username=username, paper_title=paper_title, paper_page=paper_page)
    if exist:
        exist[0].delete()
        response['msg'] = 'change note successfully'
    else:
        response['msg'] = 'add note successfully'
    note = Note.objects.create(username=username,
                               paper_title=paper_title,
                               paper_page=paper_page)
    response['error_num'] = 0
    res = JsonResponse(response)
    return res


def show_paper_detail(request):
    """
    show the paper detail
    :param request: request
    :return: response
    """
    response = {'error_num': 0, 'msg': 'success'}
    title = request.POST['title']
    username = request.POST['username']
    response['title'] = title
    paper = Paper.objects.filter(title=title, username=username)
    response['publish_time'] = paper[0].publish_time
    response['add_time'] = paper[0].add_time
    response['source'] = paper[0].source
    response['url'] = paper[0].url
    res = JsonResponse[response]
    return res


def read_paper(request):
    """
    read the paper
    :param request: request
    :return: response
    """
    response = {}
    username = request['username']
    title = request['title']
    page = request['page']
    paper = Paper.objects.filter(username=username, title=title)
    note = Note.objects.filter(username=username, paper_title=title, paper_page=page)
    response['path'] = username+'/'+title
    response['note'] = note[0].content
    res = JsonResponse[response]


def show_paper_of_the_node(request):
    """
    show the paper in the node
    :param request: request
    :return: response
    """
    response = {}
    username = request.POST['username']
    node_name = request.POST['classification_node']
    node = ClassificationTree.objects.get(username=username, name=node_name)
    papers = Paper.objects.filter(username=username, classification_tree_node=node)
    papers_title = []
    for paper in papers:
        papers_title.append(paper.title)
    response['papers_title'] = papers_title
    res = JsonResponse(response)
    return res


def show_classification_tree(request):
    """
    show the classification tree
    :param request: request
    :return: response
    """
    username = request.POST['username']
    user = Users.objects.get(username=username)
    root = user.classification_tree_root


def show_paper_of_the_subtree(request):
    """
    show the paper list of the subtree
    :param request: request
    :return: response
    """



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
