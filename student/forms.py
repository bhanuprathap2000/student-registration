from django.core import validators
from django import forms
from .models import Student

def year_check(year):
    if year>4:
        raise forms.ValidationError("Please Enter a year between 1 and 4.")

class StudentForm(forms.ModelForm):
    year=forms.IntegerField(validators=[year_check],widget=forms.NumberInput(attrs={'class':'form-control'}))
    class Meta:
        model=Student #specify the model
        fields=['name','rollnumber','email','year'] #specify the form fields
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
        'rollnumber':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        
        }
    





