#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User


# user models
class Users(User):
    head_img = models.ImageField()
    # the root the classification tree
    classification_tree_root = models.CharField(max_length=256)
    log = models.CharField(max_length=256)

    def __str__(self):
        return self.username


# user's classification tree model
class ClassificationTree(models.Model):
    username = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    father = models.CharField(max_length=256)

    def __str__(self):
        return self.name


# paper models
class Paper(models.Model):
    username = models.CharField(max_length=256)
    title = models.CharField(max_length=256)
    author = models.ManyToManyField("Author")
    publish_time = models.DateTimeField(auto_now_add=False, null=True)
    add_time = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=256, null=True)
    url = models.CharField(max_length=256)
    hash_code = models.CharField(max_length=64)
    classification_tree_node = models.CharField(max_length=256)
    file_path = models.CharField(max_length=256)
    read_status = models.IntegerField(default=0)

    def __str__(self):
        return self.title


# the author of the paper
class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()

    def __str__(self):
        return self.first_name+" "+self.last_name


# the log of the paper
class Log(models.Model):
    username = models.CharField(max_length=256)
    paper_title = models.CharField(max_length=256, blank=True)
    log = models.CharField(max_length=1024)
    add_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.log


# the notes of a paper
class Note(models.Model):
    username = models.CharField(max_length=256)
    paper_title = models.CharField(max_length=256, default="")
    paper_page = models.IntegerField(default=0)
    content = models.CharField(max_length=2048)

    def __str__(self):
        return self.paper_title+":"+str(self.paper_page)
