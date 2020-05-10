from django.forms import ModelForm
from django import forms
from contractor.models import Project

class ProjectForm(ModelForm):
	class Meta():
		model = Project
		fields = ['project_notes','project_name','project_code','project_creator','project_chat']
		widgets = {
			'project_notes': forms.HiddenInput(),
			'project_chat': forms.HiddenInput(),
			'project_code': forms.HiddenInput(),
			'project_creator': forms.HiddenInput()}

