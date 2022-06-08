from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login as loginUser, logout
from .forms import TODOForm
from .models import TODO
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def home(request):
    if request.user.is_authenticated:
        form = TODOForm()
        user = request.user
        print("this is home and you are : ",user)
        todos = TODO.objects.filter(user=user).order_by('priority')
        print("todo of the current user are  : " ,todos)
        for todo in todos:
            print(todo.task)
        countPending=TODO.objects.filter(user=user , status = 'P').count()
        print("count of taks is : ",countPending)
        context = {
        'form': form, 'todos': todos , 'countPending' : countPending}
        return render(request, "index.html", context)


def login(request):
    if request.method == 'GET':
        form1 = AuthenticationForm()
        context = {
            "form": form1
        }
        return render(request, 'login.html', context)
    else:
        form = AuthenticationForm(data=request.POST)
        # note request.post is keyword argument so we have to store in key(data)
        print(form.is_valid())
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                loginUser(request, user)
                #form = TODOForm()
                #user = request.user
                print("user logged in as  : ", user)
                context = {
                    "form": form, "username": username}
                return redirect ("home")
            
        else:
            context = {
                "form": form
            }
            return render(request, 'login.html', context=context)


def signup(request):
    if request.method == "GET":
        form = UserCreationForm()
        context = {'form': form}
        return render(request, "signup.html", context)
    else:
        print(request.POST)
        form = UserCreationForm(request.POST)
        context = {'form': form}
        if form.is_valid():
            user = form.save()
            # print(user)
            if user is not None:
                return redirect("login")
            return HttpResponse("Form is Valid")
        else:
            return render(request, "signup.html", context)

@login_required(login_url='login')
def addtodo(request):
    if request.user.is_authenticated:
        user = request.user
        print(user)
        form = TODOForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            # want to create object of formsave but not save the form in databse , this is done to add extra info later by accessing the obejct of save
            todo = form.save(commit=False)
            # here extra user is added
            todo.user = user
            todo.save()
            print(todo)
            return redirect("home")
        else:
            context = {'form': form}
            return render(request, "home.html", context)


def deletetodo(request,id):
    TODO.objects.get(id=id).delete()
    return redirect ("home")

def changestatus(request,id,status):
    todo=TODO.objects.get(id=id)
    todo.status = status
    todo.save()
    return redirect ("home")

def signout(request):
    logout(request)
    print("you are logged out")
    return redirect("login")
