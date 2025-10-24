from django.urls import path
from .import views

urlpatterns = [
     path('students/', views.student_list, name= 'student_list'),
     path('dashboard/', views.dashboard, name= 'dashboard'),
     path('students/pdf/', views.student_list_pdf, name= 'student_list_pdf'),
     path('students/excel/', views.student_list_excel, name= 'student_list_excel'),
     path('report/<int:student_id>/', views.generate_report_card, name= 'generate_report'),
]
