from django.db import models

# Create your models here.
from django.db import models

class Course(models.Model):
    course_code = models.CharField(max_length=12,)  # Unique code for the course
    course_name = models.CharField(max_length=50)
    course_description = models.TextField(blank=True)  # Use TextField for longer descriptions
    date_created = models.DateTimeField(auto_now_add=True)  # Automatically set date when created
    status = models.BooleanField(default=True)  # Active/Inactive status

    def __str__(self):
        return self.course_name

    class Meta:
        ordering = ['course_name']  # Orders courses by name by default
