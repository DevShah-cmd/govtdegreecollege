from django.urls import path
from departments.views import (
    departments_view,
    department_detail_view,
)


urlpatterns = [
    path('', departments_view),
    path('department/<int:id>/', department_detail_view),
]