from django.db import models

# Create your models here.
class employee(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    sex = models.CharField(max_length=20)
    dob = models.DateField()

    def __str__(self):
        return f"{self.firstname}, {self.lastname}, {self.sex}, {self.dob}"