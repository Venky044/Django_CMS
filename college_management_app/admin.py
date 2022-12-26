from django.contrib import admin
from .models import (Staffs, Students, Courses, Subjects, 
                    Result, MessageToStaff, MessageToStudent, 
                    Events, ContactUs)

# Register your models here.

admin.site.register(Staffs)
admin.site.register(Students)
admin.site.register(Courses)
admin.site.register(Subjects)
admin.site.register(Result)
admin.site.register(MessageToStaff)
admin.site.register(MessageToStudent)
admin.site.register(Events)
admin.site.register(ContactUs)