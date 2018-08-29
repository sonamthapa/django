from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home_view(request,*args, **kwargs):
	print(*args , **kwargs)
	print(request.user)
	#return HttpResponse('<h1> Hello World </h1>')
	return render(request,'home.html',{})

def contact_view(request,*args,**kwargs):
	#return HttpResponse('<h1>contact page </h1>')
	return render(request,'contact.html',{})

def about_view(request,*args,**kwargs):
	my_context = {
		"my_text":"this is about us",
		"my_number":123,
		"this is true":True,
		"my_list":[122344,125,5575,"sadba"]	
	}
	return render(request,'about.html', my_context)	