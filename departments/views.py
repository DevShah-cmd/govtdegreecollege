from django.http import HttpResponse
from django.shortcuts import render
from faculty.models import Staff
from downloads.models import Download
from .models import (
    Department,
    DepartmentHeader
)



# Create your views here.


def departments_view(request):
    departments = Department.objects.all()
    department_header = DepartmentHeader.objects.latest('id')
    context = {
        "departments" : departments,
        "department_header" : department_header,
    }
    return render(request, "departments/departments.html", context=context)


def department_detail_view(request, id = None):
    departments = None
    staff = None
    downloads = None
    if id is not None:
        departments = Department.objects.get(id = id)
        staff = Staff.objects.filter(department__name__contains = departments.name).order_by('number_in_order')
        downloads = Download.objects.filter(department__name__contains = departments.name)
    context = {
        "department" : departments,
        "staff" : staff,
        "downloads" : downloads,
    }
    return render(request, "departments/department.html", context=context)


