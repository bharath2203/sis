from django.contrib import admin
from .models import Student, Course, Program

class StudentAdmin(admin.ModelAdmin):

    fields = ('usn', 'student_name', 'father_name','program_taken', 
        'student_phone_no', 'father_phone_no', 'date_of_birth', 'address'
    )


admin.site.site_header = 'GECH Administration'
admin.site.site_title = 'GECH Administration'

# Register your models here.
admin.site.register(Student, StudentAdmin)
admin.site.register(Course)
admin.site.register(Program)