from django.contrib import admin
from .models import TODO

# Register your models here.

@admin.register(TODO)
class TODO (admin.ModelAdmin):
    list_display = ['task','status','date','user','priority']
