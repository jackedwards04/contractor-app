from django.db import models
from . import generate_code as gc

# Create your models here.
class Project(models.Model):
	project_name = models.CharField(max_length=100)
	project_code = models.CharField(max_length=100)
	project_creator = models.CharField(max_length=100)
	project_chat = models.TextField()
	project_notes = models.TextField()
	def get_absolute_url(self):
		return reverse('modelforms:index')