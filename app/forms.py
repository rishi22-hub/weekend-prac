# forms.py

from django import forms
from .models import Student,branch,college

class CollegeForm(forms.ModelForm):
    class Meta:
        model = college
        fields = '__all__'

class BranchForm(forms.ModelForm):
    class Meta:
        model = branch
        fields = '__all__'

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        
    # Optional: Initialize the branch field with an empty queryset
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['branch'].queryset = branch.objects.none()
