from django.db import models
from django.utils import timezone
from django.core.mail import  send_mail
from django.template.loader import render_to_string
from course.models import Course
from django.utils.html import strip_tags


class Student(models.Model):
    GENDER_CHOICES = [
        ('M','Male'),
        ('F','Female'),
        ('O','Others'),
        ('P','Prefer Not To Say')
    ]
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    addmission_no = models.PositiveIntegerField(unique=True)
    addmission_date = models.DateField()
    address = models.CharField(max_length=200, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20,null=True, blank=True)
    emergency_contact_phone = models.CharField(max_length=20)
    current_class = models.ForeignKey(Course, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    
    def full_name(self):
        """Return the full name of the student."""
        return f"{self.first_name} {self.last_name}"

    

def next_month():
    today = timezone.now()
    next_month = timezone.timedelta(days=30)
    return next_month

class StudentFee(models.Model):
    student = models.ForeignKey(Student , on_delete=models.PROTECT)
    valid_until = models.DateField(default= next_month)
    total_amount = models.PositiveIntegerField(default=0)
    date_submitted = models.DateTimeField(auto_now_add=True)
    receipt_generated = models.BooleanField(default=False)



    def __str__(self):
        return f'Fee : {self.student.full_name()} - {str(self.date_submitted)}'
    
    def generate_receipt(self):
        """Generate and send a fee receipt to the student."""
        if not self.receipt_generated:
            subject = 'Fee Receipt'
            # Render the HTML template
            html_message = render_to_string('receipt_email.html', {'fee': self})
            # Strip the HTML tags for the plain text version (optional)
            plain_message = strip_tags(html_message)
            # Send the email
            send_mail(
                subject, 
                plain_message, 
                'schoolmanagement8000@gmail.com', 
                [self.student.email], 
                html_message=html_message
            )
            self.receipt_generated = True
            self.save()
            