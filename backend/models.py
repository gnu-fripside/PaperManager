from django.db import models


class Book(models.Model):
    book_name = models.CharField(max_length=64)
    add_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.book_name


# Create your models here.
class TagTree(models.Model):
    name = models.CharField(max_length=256)
    userId = models.CharField(max_length=64)
    father = models.CharField(max_length=64)

    def __unicode__(self):
        return self.name


class Tags(models.Model):
    tag = models.CharField(max_length=1024)

    def __str__(self):
        return self.tag


class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()


class Note(models.Model):
    userId = models.CharField(max_length=64)
    paperHashCode = models.CharField(max_length=64)
    content = models.CharField(max_length=2048)
    paper = models.ManyToManyField('PaperNode')
    page = models.IntegerField()


class PaperNode(models.Model):
    title = models.CharField(max_length=256)
    author = models.ManyToManyField(Author)
    publishTime = models.DateTimeField(auto_now_add=False)
    addTime = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField(Tags)
    source = models.CharField(max_length=256)
    filePath = models.CharField(max_length=256)
    hashCode = models.CharField(max_length=64)
    notes = models.ForeignKey(Note)


class Users(models.Model):
    user_name = models.CharField(max_length=50)
    user_password = models.CharField(max_length=50)
    user_email = models.CharField(max_length=50)
    user_tag_tree = models.ForeignKey(TagTree, blank=True, null=True)
