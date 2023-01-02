from django.shortcuts import render
from .models import Download
# Create your views here.


def downloads_view(request):
    downloads = Download.objects.all()
    context = {
        "downloads" : downloads,
    }
    return render(request, "downloads/downloads.html", context=context)


# def download_detail_view(request, id = None):
#     download = None
#     if id is not None:
#         download = Download.objects.get(id = id)
#     context = {
#         "downloads" : download,
#     }
#     return render(request, "downloads/downloads.html", context=context)