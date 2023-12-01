from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # instructor = models.ForeignKey(Instructor)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    duration = models.IntegerField()
    image = models.ImageField()
    category = models.CharField(max_length=255)
    is_published = models.BooleanField()
    prerequisites = models.ManyToManyField("self")
    # symmetrical = False, blank=True, null=True
    modules = models.ManyToManyField("Module")

class Module(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    # instructor = models.ForeignKey(Instructor)
    duration = models.IntegerField()
    image = models.ImageField()
    category = models.CharField(max_length=255)
    is_published = models.BooleanField()
    thisCourse = models.ForeignKey(Course, on_delete=models.CASCADE)
    order = models.IntegerField()
    notes = models.TextField()
    files = models.FileField()
    labs = models.ManyToManyField("Lab")

class Lab(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    thisModule = models.ForeignKey(Module, on_delete=models.CASCADE)
    order = models.IntegerField()
    instructions = models.TextField()
    materials = models.TextField()
    due_date = models.DateField()
    is_completed = models.BooleanField()
    files = models.FileField()

class Submission(models.Model):
    # student = models.ForeignKey(Student)
    thisAssignment = models.ForeignKey("Assignment", on_delete=models.CASCADE)
    submission_date = models.DateTimeField()
    files = models.FileField()
    feedback = models.TextField()
    score = models.IntegerField()

class Assignment(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    due_date = models.DateField()
    instructions = models.TextField()
    max_score = models.IntegerField()
    is_published = models.BooleanField()
    files = models.FileField()
    submissions = models.ManyToManyField(Submission)

