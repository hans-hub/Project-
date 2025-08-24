from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import JobApplication, Note

@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'position', 'status', 'applied_date', 'user')
    list_filter = ('status', 'applied_date')
    search_fields = ('company_name', 'position')

@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = ('application', 'created_at')
    search_fields = ('content',)
