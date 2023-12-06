from django.contrib import admin
from .models import Course, Module, Lab, Submission, Assignment

# Register your models here.

class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "description")

class ModuleAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "description")

class LabAdmin(admin.ModelAdmin):
    list_display = ("title", "description")

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("score", "submission_date")

class AssignmentAdmin(admin.ModelAdmin):
    list_display = ("title", "this_course", "description")

admin.site.register(Course, CourseAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Lab, LabAdmin)
admin.site.register(Submission, SubmissionAdmin)
admin.site.register(Assignment, AssignmentAdmin)