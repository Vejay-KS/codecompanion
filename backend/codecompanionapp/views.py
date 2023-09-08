from django.shortcuts import  render, redirect
from codecompanionapp.signUpForm import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from rest_framework import viewsets
from .serializers import CodecompaniontestSerializer
from .models import Codecompaniontest
from codecompanionapp.ftCodeOptimizer import CodeOptimizerForm

# Create your views here.

# Test View
class CodecompaniontestView(viewsets.ModelViewSet):
    serializer_class = CodecompaniontestSerializer
    queryset = Codecompaniontest.objects.all()

app_home = "homepage"
def homepage(request):
	return render(request=request, template_name='codecompanionapp/home.html')

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect(app_home)
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="codecompanionapp/registerationPage.html", context={"registration_form":form})

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect(app_home)
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="codecompanionapp/loginPage.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect(app_home)

def code_optimizer(request):
	if request.method == "POST":
		form = CodeOptimizerForm(request.POST)
		if form.is_valid():
			input_code = form.cleaned_data.get('input_code')
			print(input_code)
			messages = [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": input_code}]
			responseFromLLM = form.generate_chat_completion(messages)
			print(responseFromLLM)
			return redirect(app_home)
	form = CodeOptimizerForm()
	return render(request=request, template_name="codecompanionapp/codeOptimizer.html", context={"codeOptimizer_form":form})
	