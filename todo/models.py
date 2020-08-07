from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    
    title = models.CharField(max_length=50)
    memo = models.TextField(blank=True, default="No Memo added")
    DateCreated = models.DateTimeField(auto_now_add=True)
    DateCompleted = models.DateTimeField(null=True, blank=True)
    important = models.BooleanField(default=False) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)  #Giving the  content specific to the user!
    
    def __str__(self):
        return self.title

