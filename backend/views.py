from django.http import JsonResponse, FileResponse, StreamingHttpResponse
from django.core import serializers
from django.contrib.auth import authenticate, login, logout
from .utils import util
from .models import *
from .utils.PaperNode import *
from .utils.ArxivScrapy import *
import json
from django.views.decorators.csrf import csrf_exempt



@csrf_exempt 
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
        response["error_num"] = 1
        response["msg"] = "The user has been registered!"
    else:
        user = Users.objects.create(username=username, password=password,
                                    email=email,
                                    classification_tree_root='root')
        ClassificationTree.objects.create(username=username, name="root")
        response['error_num'] = 0
        response['msg'] = 'success'
    return JsonResponse(response)

@csrf_exempt 
def user_login(request):
    """
    User login
    :param request: request
    :return: response{"error_num", "msg":message of errors}
    """
    response = {}
    username_ = request.POST["username"]
    password_ = request.POST["password"]
    user = Users.objects.filter(username=username_)
    if user:
        if user[0].password == password_:
            response["error_num"] = 0
            response["msg"] = "success"
        else:
            response["error_num"] = 1
            response["msg"] = "user password is wrong"
    else:
        response["error_num"] = 1
        response["msg"] = "user does not exist"
    res = JsonResponse(response)

    if response["error_num"] == 0:
        res.set_cookie("username", username_, 360001)
    return res


@csrf_exempt 
def user_logout(request):
    """
    User logout
    :param request: request
    :return: logout success Json Response
    """
    logout(request)
    response = {"error_num": 0, "msg": "logout success"}
    res = JsonResponse(response)
    return res

@csrf_exempt 
def add_classification(request):
    """
    add node in the classification tree
    :param request: request
    :return: Json response{"error_num", "msg": message of the error}
    """
    response = {}
    username = request.POST["username"]
    father_name = request.POST["father_name"]
    new_name = request.POST["name"]
    father = ClassificationTree.objects.filter(username=username, name=father_name)
    exist = ClassificationTree.objects.filter(username=username, name=new_name)
    if not father:
        response["error_num"] = 1
        response["msg"] = "the father node does not exist"
    elif exist:
        response["error_num"] = 2
        response["msg"] = "the node name had existed"
    else:
        node = ClassificationTree.objects.create(username=username,
                                                 name=new_name,
                                                 father=father_name)
        response["error_num"] = 0
        response["msg"] = "success"
    res = JsonResponse(response)
    return res

@csrf_exempt 
def add_paper(request):
    """
    add paper in one node of the classification tre
    :param request: request
    :return: later add
    """
    response = {}
    username = request.POST["username"]
    title = request.POST["title"]
    # authors = request.POST["author"]
    # publish_time = request.POST["publish_time"]
    # source = request.POST["source"]
    if Paper.objects.filter(username=username, title=title):
        response["msg"] = "the paper existed"
        response["error_num"] = 1
    else:
        url = request.POST["links"]
        file_path = "resource/tags/"+username+"/"+request.POST["file_path"]
        hash_code = paperDown(url, file_path)
        node_name = request.POST["node_name"]
        paper = Paper.objects.create(username=username, title=title,
                                    url=url, hash_code=hash_code,
                                    file_path=file_path,
                                    classification_tree_node=node_name)
        for i in range(100):
            Note.objects.create(username=username, paper_title=title, paper_page=i, content="")
        note = Note.objects.filter(username=username, paper_title=title)
        """
        for au in authors:
            author = Author.objects.filter(first_name=au["first_name"],
                                        last_name=au["last_name"],
                                        email=au["email"])
            if author:
                paper.author.add(author[0])
            else:
                new_author = Author.objects.create(first_name=au["first_name"], last_name=au["last_name"],
                                                email=au["email"])
                paper.author.add(new_author)
        """
        response["error_num"] = 0
        response["msg"] = "success"
    res = JsonResponse(response)
    Log.objects.create(username=username, paper_title=title,
                       log="add paper "+title+" in "+node_name)
    return res

@csrf_exempt 
def update_paper_info(request):
    """
    update the paper info
    :param request: request
    :return: resoponse
    """
    userid = request.POST["username"]
    title = request.POST["title"]
    publish_time = request.POST["publish_time"]
    source = request.POST["source"]
    print('authors: ', request.POST)
    author = request.POST["author"]
    author = eval(author)
    print(author)
    paper = Paper.objects.filter(username=userid, title=title)[0]
    paper.publish_time = publish_time
    paper.source = source
    paper.author.clear()
    paper.save()
    for au in author:
        author_ex = Author.objects.filter(first_name=au['first_name'],
                                          last_name=au['last_name'],
                                          email=au['email'])
        if author_ex:
            paper.author.add(author_ex[0])
        else:
            new_author = Author.objects.create(first_name=au['first_name'], last_name=au['last_name'],
                                               email=au['email'])
            paper.author.add(new_author)
    response = {"error_num": 0, "msg": "success"}
    Log.objects.create(username=userid, paper_title=title,
                       log="update the info of "+title)
    return JsonResponse(response)


def update_read_status(request):
    """
    update the read status of the paper
    :param request: request
    :return: response
    """
    username = request.GET.get("username")
    hash_code = request.GET.get("hash_code")
    paper = Paper.objects.filter(username=username, hash_code=hash_code)[0]
    paper.read_status = request.GET.get("read_status")
    paper.save()
    response = {"error_num": 0, "msg": "success"}
    Log.objects.create(username=username, paper_title=paper.title,
                       log="update the read_status of " + paper.title)
    return JsonResponse(response)

@csrf_exempt 
def save_note(request):
    """
    add and change node for a paper
    :param request: request
    :return: later add
    """
    response = {}
    username = request.POST["username"]
    hash_code = request.POST["hash_code"]
    paper_page = request.POST["paper_page"]
    note_content = request.POST["content"]
    paper = Paper.objects.filter(username=username, hash_code=hash_code)[0]
    exist = Note.objects.filter(username=username, paper_title=paper.title, paper_page=paper_page)
    if exist:
        exist[0].delete()
        response["msg"] = "change note successfully"
    else:
        response["msg"] = "add note successfully"
    note = Note.objects.create(username=username,
                               paper_title=paper.title,
                               paper_page=paper_page,
                               content=note_content)
    response["error_num"] = 0
    res = JsonResponse(response)
    Log.objects.create(username=username, paper_title=paper.title,
                       log="add note in "+paper.title+" page"+paper_page)
    return res

@csrf_exempt 
def show_paper_detail(request):
    """
    show the paper detail
    :param request: request
    :return: response
    """
    response = {"error_num": 0, "msg": "success"}
    hash_code = request.POST["hash_code"]
    username = request.POST["username"]
    paper = Paper.objects.filter(username=username, hash_code=hash_code)
    response["title"] = paper[0].title
    response["publish_time"] = paper[0].publish_time
    response["source"] = paper[0].source
    response["url"] = paper[0].url
    response["read_status"] = paper[0].read_status
    response["hash_code"] = paper[0].hash_code
    response["author"] = []
    authors = paper[0].author.all()
    for authors_ex in authors:
        tmp = {"first_name": authors_ex.first_name, "last_name": authors_ex.last_name, "email": authors_ex.email}
        response["author"].append(tmp)
    res = JsonResponse(response)
    return res

@csrf_exempt
def read_paper(request):
    """
    read the paper
    :param request: request
    :return: response
    """
    response = {}
    username = request.POST["username"]
    hash_code = request.POST["hash_code"]
    paper = Paper.objects.filter(username=username, hash_code=hash_code)[0]
    notes = Note.objects.filter(username=username, paper_title=paper.title)
    print(notes[0])
    note = []
    for note_ex in notes.all():
        tmp = {"page": note_ex.paper_page, "content": note_ex.content}
        note.append(tmp)
    # with open(os.path.join(paper.file_path, paper.hash_code+".pdf"), "rb") as f:
    #     paper_context = f.read()
    # response["paper_context"] = paper_context
    response["note"] = note
    response["read_status"] = paper.read_status
    res = JsonResponse(response)
    Log.objects.create(username=username, paper_title=paper.title,
                       log="read paper "+paper.title)
    return res

def get_paper(request):
    username = request.GET.get("username")
    hash_code = request.GET.get("hash_code")
    paper = Paper.objects.filter(username=username, hash_code=hash_code)[0]
    the_file_name = os.path.join(paper.file_path, paper.hash_code+".pdf")
    
    def file_iterator(file_name, chunk_size=512):
        with open(file_name, 'rb') as f:
            while True:
                c = f.read()
                if c:
                    yield c
                else:
                    break
    
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
 
    return response


@csrf_exempt 
def show_paper_of_the_node(request):
    """
    show the paper in the node
    :param request: request
    :return: response
    """
    response = {}
    username = request.POST["username"]
    node_name = request.POST["classification_node"]
    node = ClassificationTree.objects.get(username=username, name=node_name)
    papers = Paper.objects.filter(username=username, classification_tree_node=node)
    papers_title = []
    for paper in papers.all():
        tmp = {"paper_title": paper.title, "hash_code": paper.hash_code}
        papers_title.append(tmp)
    response["papers_title"] = papers_title
    response["error_num"]=0
    res = JsonResponse(response)
    return res


def find_son_node(username, node):
    """
    find the son node name of "node"
    :param username: username
    :param node: the node name
    :return: the son list
    """
    son_node = ClassificationTree.objects.filter(username=username, father=node)
    if son_node:
        son = []
        for son_node_ex in son_node.all():
            son_node_ex = son_node_ex.name
            tmp = {"value": son_node_ex, "label": son_node_ex, "children": []}
            tmp["children"] = find_son_node(username, tmp["label"])
            son.append(tmp)
        return son
    else:
        return []

@csrf_exempt 
def show_classification_tree(request):
    """
    show the classification tree
    :param request: request
    :return: response
    """
    username = request.GET.get("username")
    username = username.split('"')[0]
    print(username)
    user = Users.objects.get(username=username)
    root = user.classification_tree_root
    node = {"value": root, "label": root, "children": find_son_node(username, root)}
    response = {"node": [node]}
    res = JsonResponse(response)
    return res


def find_son_paper(username, node_name):
    """
    find the papers in the son node of the node_name
    :param username: username
    :param node_name: the name of the node
    :return: the title of the papers
    """
    sons = ClassificationTree.objects.filter(username=username, father=node_name)
    paper_title = []
    if sons:
        for sons_ex in sons.all():
            papers = Paper.objects.filter(username=username, classification_tree_node=sons_ex.name)
            for paper in papers.all():
                paper_title.append(paper.title)
            paper_title.extend(find_son_paper(username, sons_ex.name))
    return paper_title

@csrf_exempt 
def show_paper_of_the_subtree(request):
    """
    show the paper list of the subtree
    :param request: request
    :return: the paper title in the subtree
    """
    username = request.POST["username"]
    node_name = request.POST["node_name"]
    papers = Paper.objects.filter(username=username, classification_tree_node=node_name)
    papers_title = []
    if papers:
        for paper in papers.all():
            papers_title.append(paper.title)
    papers_title.extend(find_son_paper(username, node_name))
    return papers_title


def getTagList(request):
    userId = request.GET.get("userId")
    currentPath = request.GET.get("currentPath")
    response = util.getTagList(userId, currentPath)
    return JsonResponse(response)


def getFileList(request):
    userId = request.GET.get("userId")
    currentPath = request.GET.get("currentPath")
    response = util.getFileList(userId, currentPath)
    return JsonResponse(response)


def sub_tree_paper_pack(request):
    """
    pack the sub tree paper
    :param request: request
    :return: response
    """
    username = request.GET.get("username")
    current_path = request.GET.get("currentPath")
    temp_dir = "../resource/temp"
    output_dir = "../resource/tags/"+username+"/outputDir"
    the_file_name = util.SubTreePack(current_path, username, temp_dir, output_dir)
    the_file_name = "backend/resource/tags/" + username + "/" + the_file_name

    def file_iterator(output_path, chunk_size=512):
        with open(output_path) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    return response


def paper_node_pack(request):
    """
    pack the paper standard documentation
    :param request: request
    :return: response
    """
    username = request.GET.get("username")
    paper_title = request.GET.get("paper_title")
    paper = Paper.objects.filter(username=username, paper_title=paper_title)[0]
    notes = Note.objects.filter(username=username, paper_title=paper_title)
    logs = Log.objects.filter(username=username, paper_title=paper_title)
    authors = []
    for author_ex in paper.author.all():
        tmp = {"first_name": author_ex.first_name,
               "last_name": author_ex.last_name,
               "email": author_ex.email}
        authors.append(tmp)
    paper_node = PaperNode(username, paper_title, authors, paper.publish_time, paper.add_time,
                           paper.classification_tree_node, paper.source, paper.url, paper.file_path,
                           paper.read_status)
    note = []
    for note_ex in notes.all():
        tmp = {"username": username, "paper_title": paper_title,
               "paper_page": note_ex.paper_page,
               "context": note_ex.content}
        note.append(tmp)
    log = []
    for logs_ex in logs.all():
        tmp = {"username": username, "paper_title": logs_ex.paper_title,
               "log_context": logs_ex.log,
               "add_time": logs_ex.add_time}
        log.append(tmp)
    temp_dir = "../resource/tags/tmp"
    output_dir = "../resource/tags/"+username+"/outputDir"
    the_file_name = util.PaperNodePack(paper_node, username, temp_dir, output_dir, note, log)
    the_file_name = "backend/resource/tags/"+username+"/"+the_file_name

    def file_iterator(output_path, chunk_size=512):
        with open(output_path) as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break

    response = StreamingHttpResponse(file_iterator(the_file_name))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
    return response

