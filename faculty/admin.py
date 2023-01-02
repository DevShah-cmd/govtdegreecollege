from django.contrib import admin
from .models import (
    Staff,
    StaffHeader
)

# Register your models here.
admin.site.register(Staff)
admin.site.register(StaffHeader)