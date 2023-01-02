from django.urls import path
from core.views import (
    index_view,
    notice_detail_view,
    news_detail_view,
    merit_list_view,
    about_view,
)

urlpatterns = [
    path('', index_view),
    path('notice/<int:id>', notice_detail_view),
    path('news/<int:id>', news_detail_view),
    path('about/', about_view),
    path('meritlist/<int:pk>', merit_list_view),
]
