from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm



def dashboard(request):
	return render(request,'account/dashboard.html')

def user_login(request):
	form = LoginForm()
	if request.method == 'POST':
		if form.is_valid():
			form = LoginForm(request.POST)
			cd = form.cleaned_data
			username = cd['username']
			password = cd['password']
			user = authenticate(request,username,password)

			if user is not None:
				if user.is_active():
					login(request,user)
					return HttpResponse("user authenticated successfully")
				else:
					return HttpResponse('Invalid login')



	return render(request,'account/login.html',{'form':form})
