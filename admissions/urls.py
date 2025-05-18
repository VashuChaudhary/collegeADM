from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('courses/', views.CourseListView.as_view(), name='course_list'),
    path('apply/', views.AdmissionApplicationView.as_view(), name='apply'),
    path('success/', views.ApplicationSuccessView.as_view(), name='application_success'),
    path('status/<str:email>/<int:application_id>/', 
         views.ApplicationStatusView.as_view(), name='application_status'),
]
