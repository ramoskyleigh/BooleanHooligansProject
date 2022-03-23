from django.http import HttpResponse
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import login, authenticate 

global is_student
is_student = True
#issue is that this is the boolean being sent to both login and register views

def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})
	
def register_view(request, *args, **kwargs):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		print(form)
		if form.is_valid():
			user = form.save()
			login(request, user)
			userType = form.cleaned_data.get('user_type')
			print(userType)
			if userType == 'Student':
				is_student == True
				print('this is working')
				return redirect(studentDashboard_view)
			else: 
				is_student == False
				print('bool was switched in register')
				return redirect(profDashboard_view)

			messages.success(request, "Registration successful." )
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request, "register.html",{"register_form":form}, is_student)

def login_view(request, *args, **kwargs):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			userType = form.cleaned_data.get('user_type')
			user = authenticate(username=username, password=password)

			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				if userType == 'Student':
					is_student == True
					print('this is working')
					return redirect(studentDashboard_view)
				else: 
					is_student == False
					print('bool was switched in login')
					return redirect(profDashboard_view)
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request, "login.html" ,{"login_form":form})


def logout_view(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect(home_view)

def dashboard_view(request, *args, **kwards):
	return render (request, "dashboard.html")	

def studentDashboard_view(request, *args, **kwards):
	return render (request, "studentDashboard.html")	

def profDashboard_view(request, *args, **kwards):
	return render (request, "professorDashboard.html")	
