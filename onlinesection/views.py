from django.shortcuts import render
from .models import (
    OnlineSection
)
# Create your views here.



def onlinesection_view(request):
    online_sections = OnlineSection.objects.filter().order_by('-id')
    # online_sections = OnlineSection.objects.order_by('-created_date')
    # online_sections = OnlineSection.objects.latest('title')
    # online_section = OnlineSection.objects.all()
    context = {
        "onlinesections" : online_sections,
    }
    return render(request, "onlinesection/onlinesection.html", context=context)


def onlinesection_detail_view(request, id = None):
    online_section = None
    if id is not None:
        online_section = OnlineSection.objects.get(id = id)
    context = {
        "onlinesection" : online_section,
    }
    return render(request, "onlinesection/online-page.html", context=context)