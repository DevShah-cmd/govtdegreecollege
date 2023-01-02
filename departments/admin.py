from django.contrib import admin
from .models import (
    Department,
    DepartmentHeader
)

# Register your models here.
admin.site.register(Department)
admin.site.register(DepartmentHeader)