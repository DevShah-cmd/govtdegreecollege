from django.urls import path
from onlinesection.views import (
    onlinesection_view,
    onlinesection_detail_view
)



urlpatterns = [
    path('section/<int:id>/', onlinesection_detail_view),
    path('', onlinesection_view),
    
]
