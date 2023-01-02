from django.shortcuts import render
from django.http import HttpResponse
from departments.models import Department, DepartmentHeader

from .models import (
    Staff,
    StaffHeader
)
# Create your views here.


def faculty_view(request):
    # faculties = Staff.objects.all()
    faculties = Staff.objects.filter().order_by('number_in_order')
    departments_list = Department.objects.all()
    faculty_header = DepartmentHeader.objects.latest('id')
    context = {
        "faculties" : faculties,
        "faulty_header" : faculty_header,
    }
    return render(request, "faculty/faculty.html", context=context)


def staff_detail_view(request, id = None):
    faculty_header = None
    staff = None
    # faculty_header = DepartmentHeader.objects.latest('id')
    if id is not None:
        staff = Staff.objects.get(number_in_order = id)
        faculty_header = StaffHeader.objects.latest('id')

    context = {
        "staff" : staff,
        "faulty_header" : faculty_header,
    }
    return render(request, "faculty/staff.html", context=context)
