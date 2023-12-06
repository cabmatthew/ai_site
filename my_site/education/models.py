from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True) 
    description = models.TextField(null=True, blank=True)
    # instructor = models.ForeignKey(Instructor)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    duration = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    is_published = models.BooleanField(null=True, blank=True)
    this_prerequisites = models.ManyToManyField("self", null=True, blank=True)
    # symmetrical = False, blank=True, null=True
    this_modules = models.ManyToManyField("Module", null=True, blank=True)

class Module(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    # instructor = models.ForeignKey(Instructor)
    duration = models.IntegerField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    category = models.CharField(max_length=255, null=True, blank=True)
    is_published = models.BooleanField(null=True, blank=True)
    this_course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    files = models.FileField(null=True, blank=True)
    this_labs = models.ManyToManyField("Lab", null=True, blank=True)

class Lab(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    this_module = models.ForeignKey(Module, on_delete=models.CASCADE, null=True, blank=True)
    order = models.IntegerField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    materials = models.TextField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    is_completed = models.BooleanField(null=True, blank=True)
    files = models.FileField(null=True, blank=True)

class Submission(models.Model):
    # student = models.ForeignKey(Student)
    this_assignment = models.ForeignKey("Assignment", on_delete=models.CASCADE, null=True, blank=True)
    submission_date = models.DateTimeField(null=True, blank=True)
    files = models.FileField(null=True, blank=True)
    feedback = models.TextField(null=True, blank=True)
    score = models.IntegerField(null=True, blank=True)

class Assignment(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    this_course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    instructions = models.TextField(null=True, blank=True)
    max_score = models.IntegerField(null=True, blank=True)
    is_published = models.BooleanField(null=True, blank=True)
    files = models.FileField(null=True, blank=True)
    this_submissions = models.ManyToManyField(Submission, null=True, blank=True)


