from django.contrib import admin
from .models import book, userprefbook

# Register your models here.
admin.site.register(book)
admin.site.register(userprefbook)