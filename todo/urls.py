from django.urls import path
from . import views

urlpatterns = [
    
    #AUTH   
    
    path("",views.homepage,name="homepage"), #Home page
    path("register/",views.register,name="home"), #Sign up page
     path("about/",views.about,name="about"), # About page
    
    path("logout/",views.logout,name="logout"), #Logout Page
    path("login/",views.login,name="login"), # login page
     path("joke/",views.joke,name="joke"), # login page
    
    #TODO
    
    path("create/",views.createTodo,name="create"), #Creating TODO
    path("<int:id>/",views.createTodo,name="update"), #UPDATING TODO
    path("list/",views.todoList,name="list"), #LISTING ALL TODOS
   
    path("delete/<int:id>/",views.delete,name="delete"), #Deleting the TODO
]
