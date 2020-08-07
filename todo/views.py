from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User,auth,AnonymousUser
from django.db import IntegrityError
from .form import TodoForm
from .models import Todo
from django.utils import timezone
import pyjokes
# Create your views here.

#HOME PAGE OF THE WEBSITE   
def joke(request):
    jokes = pyjokes.get_joke()
    return render(request,"jokes.html",{"joke":jokes})
def homepage(request):
    
    return render(request,"home.html")

# Signup Section

def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]
        
        if pass1 == pass2:
            try:
                user = User.objects.create_user(username=username, email= email, password=pass1,first_name=first_name)
                user.save()
                return redirect("login")
            except ValueError:
                messages.info(request,"Username already Taken")
                return redirect("home")
        else:
            messages.info(request,"Passwords are not matching")        
            return redirect ("home")        
    return render(request,"register.html")



#Login Section


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        pass1 = request.POST["pass1"]
        
            
        user = auth.authenticate(username= username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return redirect("list")
        messages.info(request,"invalid Credentials!")
        return redirect("login")    
    return render(request,"login.html")


#LOGOUT Section

def logout(request):
    auth.logout(request)
    return redirect("homepage")



#Creatin/Adding the TODO



def createTodo(request,id=0):
    form = TodoForm()
    if request.method == "GET":
        if id == 0:
            form = TodoForm()
            
        else:
            update = Todo.objects.get(pk = id)
            form = TodoForm(instance=update)
        return render(request,"todo.html",{"form":form})
    else:
        
        if id == 0:

                   
            form = TodoForm(request.POST )
            newTodo = form.save(commit=False)
            newTodo.user = request.user
            newTodo.save()
            return redirect("list") 
            # form = Todo.objects.filter(user = request.user)
            # form.save()

            print("NOT posted")
# This part is not working

        else: 
            update = Todo.objects.get(pk = id)
            form = TodoForm(request.POST,instance=update)
            newTodo = form.save(commit=False)
            newTodo.user = request.user
            newTodo.save()
            print("posted")
            return redirect("list")    
    return render(request,"todo.html",{"form":form})




#Listing all the added TODOS



def todoList(request):
    
    form = Todo.objects.filter(user=request.user)
    return render(request,"list.html",{"list":form})
    
    

#Deleting the TODO
    
 

def delete(request,id):
    form = Todo.objects.get(pk=id)
    form.delete()
    return redirect("list")



#About Page of Author



def about(request):
    return render(request,"about.html")







