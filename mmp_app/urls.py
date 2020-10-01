from django.urls import path,include
from mmp_app import views

app_name='mmp_app'

urlpatterns=[
	path('faculty_login',views.faculty_login,name='faculty_login'),
    path('student_login',views.student_login,name='student_login'),
    path('faculty_register',views.faculty_register,name='faculty_register'),
    path('student_register',views.student_register,name='student_register'),
]