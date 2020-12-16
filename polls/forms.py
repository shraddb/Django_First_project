from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
	name=forms.CharField(
	widget=forms.TextInput(attrs={
		'placeholder' :'Enter ur name ',
		'class' : 'form-control'
		}))
	age=forms.IntegerField(
		widget=forms.NumberInput(attrs={
			'placeholder': 'Enter ur age ',
			'class': 'form-control'
		}))
	role=forms.CharField(
	widget=forms.TextInput(attrs={
		'placeholder' :'Enter ur role ',
		'class' : 'form-control'
		}))
	salary=forms.FloatField(
		widget=forms.NumberInput(attrs={
			'placeholder': 'Enter ur salary ',
			'class': 'form-control'
		}))

	class Meta:
		model=Employee
		fields='__all__'

