from django import forms
from .models import Student

class StudentAdminForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'gender': forms.RadioSelect,
        }
