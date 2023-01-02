from django.urls import path
from faculty.views import (
    faculty_view,
    staff_detail_view
)



urlpatterns = [
    path('faculty/<int:id>/', staff_detail_view),
    path('faculty/', faculty_view),
]
