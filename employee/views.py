from django.shortcuts import render, redirect
from .forms import EmployeeForm

def register_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = EmployeeForm()
    return render(request, 'employee/register.html', {'form': form})

def registration_success(request):
    return render(request, 'employee/success.html')

# Create your views here.
