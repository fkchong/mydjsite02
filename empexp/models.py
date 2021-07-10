from django.db import models
from django.contrib.auth.models import User
from site02.models import employee

# Create your models here.
class experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    employee = models.OneToOneField(employee, on_delete=models.CASCADE)
    companyname = models.CharField(max_length=200)
    fromdate = models.DateField()
    todate = models.DateField()
    rolesandresponsibility = models.TextField()
    reasonofleaving = models.TextField()
    currentexperience = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user.username}, {self.currentexperience}"