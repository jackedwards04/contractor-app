from django.contrib import admin
from django.forms import ModelForm
# Register your models here.
from . import models

admin.site.register(models.Project)