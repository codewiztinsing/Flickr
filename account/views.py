from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from .forms import LoginForm,RegistertionForm



def dashboard(request):
	return render(request,'account/dashboard.html')


# user  registertion
def register(request):
	form = RegistertionForm()
	if request.method == 'POST':
		if form.is_valid():
			form = RegistertionForm(request.POST)
			user = form.save(commit = False)
			password = form['password']
			user.set_password(password)
			user.save()
			return user

	return render(request,'account/register.html',{'form':form})



# user login authenticatio
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
