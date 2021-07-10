from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class book(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publishyear = models.DateField()

    def __str__(self):
        return f"{self.name}, {self.author}"

class userprefbook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bookname = models.ManyToManyField(book)
    remark = models.TextField(null=True)
    createddate = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}, {self.bookname}"
