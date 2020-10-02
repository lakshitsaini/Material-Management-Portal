from django.contrib import admin
from mmp_app.models import Course,UploadFile,Student,Faculty
# Register your models here.

admin.site.register(Course)
admin.site.register(UploadFile)
admin.site.register(Student)
admin.site.register(Faculty)