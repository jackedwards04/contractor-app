from contractor.models import Project

def getByCode(code):
	return(Project.objects.filter(project_code=code))