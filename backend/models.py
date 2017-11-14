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

class Author(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField()

class Note(models.Model):
    userId = models.CharField(max_length=64)
    paperHashCode = models.CharField(max_length=64)
    content = models.CharField(max_length=2048)

class PaperNode(models.Model):
    title = models.CharField(max_length=256)
    #############################################
    # TODO change author and add tags list
    # authors = models.ManyToManyField(Author)
    # tags = models.ManyToManyField(tag), tag is't completed
    # notes = models.ForeignKey(Note)
    #############################################
    author = models.CharField(max_length=512)
    publishTime = models.DateTimeField(auto_now_add=False)
    addTime = models.DateTimeField(auto_now_add=True)
    tags = models.CharField(max_length=1024)
    source = models.CharField(max_length=256)
    filePath = models.CharField(max_length=256)
    hashCode = models.CharField(max_length=64)
