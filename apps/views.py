from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView

from apps.models import Employee


# Create your views here.

class EmployeeView(ListView):
    template_name = 'apps/contacts-list-table.html'
    queryset = Employee.objects.order_by('-created_at')
    context_object_name = 'employees'



def index(request):
    return render(request, 'apps/update.html')


def delete_employee(request, pk):
    Employee.objects.filter(id=pk).delete()
    return redirect('employees_list_page')

def update_employee(request, pk):

    Employee.objects.filter(id=pk).update(
        name=request.POST.get('name'),
        position=request.POST.get('position'),
        email=request.POST.get('email'),
        projects=request.POST.get('projects'),
        image=request.POST.get('image')
    )
    return redirect('employees_list_page')