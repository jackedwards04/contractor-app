from contractor.models import Project

def cleanProjects():
	Project.objects.all().delete()
	return True