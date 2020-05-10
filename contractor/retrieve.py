from contractor.models import Project

def retrieveAll(user):
	return(Project.objects.filter(project_creator=user))