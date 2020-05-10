from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from customer.retrievecust import getByCode

	
def landing(request):
	request.session['test'] = 'AUCLYLBY'
	print('set session',request.session['test'])
	return render(request,"customerlanding.html")

from .forms import CodeForm

def entercode(request):
	print('prepare debug')
	if request.method == 'POST':
		form = CodeForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('/projectview/')
	else:
	  form = CodeForm()	
	return render(request, 'entercode.html', {'form': form})

def projectview(request):
	if 'your_code' in request.POST.keys():
		cust_code = request.POST['your_code']
		request.session['cust_code'] = cust_code
	else:
		cust_code = request.session['cust_code']
	print('CURRENT CODE:',cust_code)
	try:
		proj = getByCode(cust_code)[0]
	except:
		return HttpResponseRedirect('/customer/oops')
	print(proj)
	if request.method == 'POST' and 'new_message' in request.POST.keys() and not proj.project_chat.split('\n')[-1]=="Customer: " + request.POST['new_message']:
		message = request.POST['new_message']
		message = "\nCustomer: " + message
		proj.project_chat += message
		proj.save()
	context = {
			"project": proj,
			"chat": proj.project_chat.split('\n')
	}
	return render(request, "custprojectview.html", context)

def codefail(request):
	return render(request, "custfailcode.html")