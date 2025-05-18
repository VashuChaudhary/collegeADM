from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Course, AdmissionApplication
from django.views import View
from django import forms

class HomeView(ListView):
    model = Course
    template_name = 'admissions/home.html'
    context_object_name = 'courses'

class CourseListView(ListView):
    model = Course
    template_name = 'admissions/course_list.html'
    context_object_name = 'courses'

class AdmissionApplicationView(CreateView):
    model = AdmissionApplication
    template_name = 'admissions/application_form.html'
    fields = ['first_name', 'last_name', 'email', 'phone', 'date_of_birth', 
              'address', 'previous_school', 'grade_10_percentage', 
              'grade_12_percentage', 'course', 'birth_certificate', 
              'marksheet_10', 'marksheet_12']
    success_url = reverse_lazy('application_success')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        for field in form.fields.values():
            if isinstance(field.widget, forms.TextInput) or \
               isinstance(field.widget, forms.EmailInput) or \
               isinstance(field.widget, forms.DateInput) or \
               isinstance(field.widget, forms.NumberInput) or \
               isinstance(field.widget, forms.Select):
                field.widget.attrs.update({'class': 'form-control'})
            elif isinstance(field.widget, forms.Textarea):
                field.widget.attrs.update({'class': 'form-control', 'rows': 3})
            elif isinstance(field.widget, forms.FileInput):
                field.widget.attrs.update({'class': 'form-control'})
        return form

    def form_valid(self, form):
        messages.success(self.request, 'Your application has been submitted successfully!')
        return super().form_valid(form)

class ApplicationSuccessView(View):
    def get(self, request):
        return render(request, 'admissions/application_success.html')

class ApplicationStatusView(DetailView):
    model = AdmissionApplication
    template_name = 'admissions/application_status.html'
    context_object_name = 'application'

    def get_object(self, queryset=None):
        return AdmissionApplication.objects.get(
            email=self.kwargs['email'],
            id=self.kwargs['application_id']
        )
