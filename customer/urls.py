from django.urls import path
from . import views

urlpatterns = [
	path('landing', views.landing, name="custLand"),
	path('code',views.entercode,name='codeEnter'),
	path('projectview/',views.projectview),
	path('oops/',views.codefail,name="codefail")
]