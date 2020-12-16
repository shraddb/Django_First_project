from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Employee
from .forms import EmployeeForm
from django.contrib import messages


def index(request):
	return HttpResponse("<marquee><h1>Welcome to web</h1></marquee>")
	
def employee(request):
	emp=Employee.objects.all()
	context= {'emp':emp}
	return render(request,'polls/employee.html',context)

def detail(request,id):
	emp=get_object_or_404(Employee,pk=id)
	return render(request ,'polls/detail.html',{'emp':emp})

def insert(request,uid=1):
	if request.method=='POST':
		inform=EmployeeForm(request.POST)
		if inform.is_valid():
			inform.save()
			message.info(request,'Informatin stored succesfully')
			return redirect(insert)
		else:
			messages.info(request,'Invalid data')
			return redirect(insert)
	else:
		inform=EmployeeForm()
		return render(request,'polls/insert.html',{'inform':inform})








		