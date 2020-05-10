from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context
from contractor.forms import ProjectForm
from contractor.models import Project
from contractor.retrieve import retrieveAll
from contractor.generate_code import newCode
# Create your views here.

def landing(request):
	return render(request,"contractorlanding.html")

def home(request):
	context = {"username": request.user.username}
	return render(request,"contractorhomepage.html",context=context)

def newproject(request):
	if request.method == "POST":
		form = ProjectForm(request.POST)
		if form.is_valid():
			form.save()
			context = {
				"code": request.POST["project_code"]
			}
			return render(request, "newproject.html", context)
	else:
		form = ProjectForm(initial={
			'project_chat': "Welcome to the chat",
			'project_code': newCode(), 
			"project_creator": request.user.username,
			'project_notes': "Personal notes can go here"
			})
	context = {
		"form": form
	}
	return render(request, 'createproject.html', context)

def contrproject(request,code):
	print(code)
	user = request.user.username
	if len(Project.objects.filter(project_code = code)) == 0:
		return render(request, 'contrfailaccess.html')
	elif Project.objects.filter(project_code = code)[0].project_creator == user:
		currProject = Project.objects.filter(project_code = code)[0]
		print('accessing project debug',dir(currProject))
		if request.method == 'POST' and 'new_message' in request.POST.keys() and not currProject.project_chat.split('\n')[-1]==request.user.username+" (Contractor): " + request.POST['new_message']:
			message = request.POST['new_message']
			message = '\n' + request.user.username+" (Contractor): " + message
			currProject.project_chat += message
			currProject.save()
		if request.method == 'POST' and 'new_notes' in request.POST.keys():
			notes = request.POST['new_notes']
			currProject.project_notes = notes
			currProject.save()
		context = {
			"project": currProject,
			"chat": currProject.project_chat.split('\n'),
			"notes": currProject.project_notes,
		}
		return render(request, 'contrprojectview.html', context)
	else:
		return render(request, 'contrfailaccess.html')


def viewprojects(request):
	user = request.user.username
	pList = retrieveAll(user)
	print('DEBUG')
	context = {
		"user": request.user.username,
		"projects": pList
	}
	return render(request, "projectlist.html", context)