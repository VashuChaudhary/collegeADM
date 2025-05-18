from django.contrib import admin
from .models import Course, AdmissionApplication

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'seats')
    search_fields = ('name', 'code')

@admin.register(AdmissionApplication)
class AdmissionApplicationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'course', 'status', 'applied_date')
    list_filter = ('status', 'course', 'applied_date')
    search_fields = ('first_name', 'last_name', 'email')
    readonly_fields = ('applied_date',)
