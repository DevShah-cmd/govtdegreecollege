from django.urls import path
from downloads.views import (
    downloads_view
)


urlpatterns = [
    path('', downloads_view),
]