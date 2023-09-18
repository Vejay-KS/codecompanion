from django.shortcuts import  render, redirect
from codecompanionapp.signUpForm import NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from rest_framework import viewsets
from .serializers import CodecompaniontestSerializer
from .models import Codecompaniontest, CodeCompanionUser
from codecompanionapp import FilesHandler, ftCodeOptimizer, ftDocumentationHelper, ftCodeDebugger, ftCodeReviewer, ftCommentGenerator, ftLearningPathRecommendations, ftLetterGenerator, ftResumeFilterer, ftSummarizeAppraisals, ftTechnicalTrends, ftUnitTestGenerator

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
		form = ftCodeOptimizer.CodeOptimizerForm(request.POST)
		if form.is_valid():
			input_code = form.cleaned_data.get('input_code')
			print(input_code)
			messages = [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": input_code}]
			responseFromLLM = form.generate_chat_completion(messages)
			print(responseFromLLM)
			return redirect(app_home)
	form = ftCodeOptimizer.CodeOptimizerForm()
	return render(request=request, template_name="codecompanionapp/codeOptimizer.html", context={"codeOptimizer_form":form})


def documentation_helper(request):
	if request.method == "POST":
		form = ftDocumentationHelper.DocumentationHelperForm(request.POST, request.FILES)
		print("post")
		print(form.errors)
		if form.is_valid():
			print("form_valid")
			input_file = request.FILES['input_file']
			print("File received")
			#messages = [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": input_code}]
			responseFromLLM = form.generate_chat_completion(input_file)
			print(responseFromLLM)
			return redirect(app_home)
	form = ftDocumentationHelper.DocumentationHelperForm()
	return render(request=request, template_name="codecompanionapp/documentationHelper.html", context={"documentationHelper_form":form})


def resume_filterer(request):
	if request.method == "POST":
		form = ftResumeFilterer.ResumeFiltererForm(request.POST, request.FILES)
		print("post")
		print(form.errors)
		if form.is_valid():
			print("form_valid")
			input_file1 = request.FILES['input_file1']
			input_file2 = request.FILES['input_file2']
			input_file3 = request.FILES['input_file3']
			input_file = FilesHandler.FileHandler.read_file(input_file1) + '\n' + FilesHandler.FileHandler.read_file(input_file2) + '\n' + FilesHandler.FileHandler.read_file(input_file3)
			print("Files received")
			#messages = [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": input_code}]
			responseFromLLM = form.generate_chat_completion(input_file)
			print(responseFromLLM)
			return redirect(app_home)
	form = ftResumeFilterer.ResumeFiltererForm()
	return render(request=request, template_name="codecompanionapp/resumeFilterer.html", context={"resumeFilterer_form":form})

def code_debugger(request):
	if request.method == "POST":
		form = ftCodeDebugger.CodeDebuggerForm(request.POST)
		if form.is_valid():
			input_code = form.cleaned_data.get('input_code')
			print(input_code)
			messages = [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": input_code}]
			responseFromLLM = form.generate_chat_completion(messages)
			print(responseFromLLM)
			return redirect(app_home)
	form = ftCodeDebugger.CodeDebuggerForm()
	return render(request=request, template_name="codecompanionapp/codeDebugger.html", context={"codeDebugger_form":form})

def code_reviewer(request):
	if request.method == "POST":
		form = ftCodeReviewer.CodeReviewerForm(request.POST)
		if form.is_valid():
			input_code = form.cleaned_data.get('input_code')
			print(input_code)
			messages = [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": input_code}]
			responseFromLLM = form.generate_chat_completion(messages)
			print(responseFromLLM)
			return redirect(app_home)
	form = ftCodeReviewer.CodeReviewerForm()
	return render(request=request, template_name="codecompanionapp/codeReviewer.html", context={"codeReviewer_form":form})

def comment_generator(request):
	if request.method == "POST":
		form = ftCommentGenerator.CommentGeneratorForm(request.POST)
		if form.is_valid():
			input_code = form.cleaned_data.get('input_code')
			print(input_code)
			messages = [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": input_code}]
			responseFromLLM = form.generate_chat_completion(messages)
			print(responseFromLLM)
			return redirect(app_home)
	form = ftCommentGenerator.CommentGeneratorForm()
	return render(request=request, template_name="codecompanionapp/commentGenerator.html", context={"commentGenerator_form":form})


def documentation_helper(request):
	if request.method == "POST":
		form = ftDocumentationHelper.DocumentationHelperForm(request.POST)
		if form.is_valid():
			input_code = form.cleaned_data.get('input_code')
			print(input_code)
			messages = [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": input_code}]
			responseFromLLM = form.generate_chat_completion(messages)
			print(responseFromLLM)
			return redirect(app_home)
	form = ftDocumentationHelper.DocumentationHelperForm()
	return render(request=request, template_name="codecompanionapp/documentationHelper.html", context={"documentationHelper_form":form})

def learning_path_recommendation(request):
	if request.method == "POST":
		form = ftLearningPathRecommendations.LearningPathRecommendationsForm(request.POST)
		if form.is_valid():
			input_code = form.cleaned_data.get('input_code')
			print(input_code)
			messages = [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": input_code}]
			responseFromLLM = form.generate_chat_completion(messages)
			print(responseFromLLM)
			return redirect(app_home)
	form = ftLearningPathRecommendations.LearningPathRecommendationsForm()
	return render(request=request, template_name="codecompanionapp/learningPathRecommendations.html", context={"learningPathRecommendations_form":form})

def letter_generator(request):
	if request.method == "POST":
		form = ftLetterGenerator.LetterGeneratorForm(request.POST)
		if form.is_valid():
			input_code = form.cleaned_data.get('input_code')
			print(input_code)
			messages = [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": input_code}]
			responseFromLLM = form.generate_chat_completion(messages)
			print(responseFromLLM)
			return redirect(app_home)
	form = ftLetterGenerator.LetterGeneratorForm()
	return render(request=request, template_name="codecompanionapp/letterGenerator.html", context={"letterGenerator_form":form})

def summarize_appraisals(request):
	if request.method == "POST":
		form = ftSummarizeAppraisals.SummarizeAppraisalsForm(request.POST)
		if form.is_valid():
			input_code = form.cleaned_data.get('input_code')
			print(input_code)
			messages = [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": input_code}]
			responseFromLLM = form.generate_chat_completion(messages)
			print(responseFromLLM)
			return redirect(app_home)
	form = ftSummarizeAppraisals.SummarizeAppraisalsForm()
	return render(request=request, template_name="codecompanionapp/summarizeAppraisals.html", context={"summarizeAppraisals_form":form})

def technical_trends(request):
	if request.method == "POST":
		form = ftTechnicalTrends.TechnicalTrendsForm(request.POST)
		if form.is_valid():
			input_code = form.cleaned_data.get('input_code')
			print(input_code)
			messages = [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": input_code}]
			responseFromLLM = form.generate_chat_completion(messages)
			print(responseFromLLM)
			return redirect(app_home)
	form = ftTechnicalTrends.TechnicalTrendsForm()
	return render(request=request, template_name="codecompanionapp/technicalTrends.html", context={"technicalTrends_form":form})

def unit_test_generator(request):
	if request.method == "POST":
		form = ftUnitTestGenerator.UnitTestGeneratorForm(request.POST)
		if form.is_valid():
			input_code = form.cleaned_data.get('input_code')
			print(input_code)
			messages = [{"role": "system", "content": "You are a helpful assistant."},{"role": "user", "content": input_code}]
			responseFromLLM = form.generate_chat_completion(messages)
			print(responseFromLLM)
			return redirect(app_home)
	form = ftUnitTestGenerator.UnitTestGeneratorForm()
	return render(request=request, template_name="codecompanionapp/unitTestGenerator.html", context={"unitTestGenerator_form":form})