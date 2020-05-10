from django.urls import path
from . import views

urlpatterns = [
	path('landing',views.landing,name="contrLand"),
	path('home',views.home,name="contrHome"),
	path('newproject',views.newproject,name="newproject"),
	path('viewprojects',views.viewprojects,name="projectlist"),
	path('project/<str:code>',views.contrproject,name="projectview")
]