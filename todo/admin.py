from django.contrib import admin
from .models import Todo
# Register your models here.
class created(admin.ModelAdmin):
    readonly_fields = ("DateCreated",)

admin.site.register(Todo, created)