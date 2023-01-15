from django.http import HttpResponse
from django.shortcuts import render
from .models import (
    About,
    Action,
    CampusLife,
    FormerPrincipal,
    Notice,
    MeritList,
    Event,
    OurValues,
    OurVision,
    Principal,
    Header,
    Video,
    News
)


# Create your views here.


def index_view(request):
    # all_news = News.objects.all()
    all_notices = Notice.objects.all()
    newest_news = News.objects.filter().order_by('-id')
    newest_notice = Notice.objects.filter().order_by('-id')
    events_newest = Event.objects.filter().order_by('-id')
    principal = Principal.objects.latest('id')
    our_vision = OurVision.objects.latest('id')
    # about = About.objects.latest('id')
    about = About.objects.latest('id')
    actions = Action.objects.filter().order_by('-id')
    # header = Header.objects.latest('id')
    header = Header.objects.all()
    campus_life = CampusLife.objects.filter().order_by('-id')
    

    context = {
        "news" : newest_news,
        "notices" : newest_notice,
        "events" : events_newest,
        "principal" : principal,
        "our_vision" : our_vision,
        "about" : about,
        "actions" : actions,
        "header" : header,
        "campus_life_s" : campus_life,
    }
    return render(request, "core/index.html", context=context)


def news_detail_view(request, id = None):
    news = None
    if id is not None:
        news = News.objects.get(id = id)
    context = {
        "news" : news,
    }
    return render(request, "core/newspage.html", context=context)


def notice_detail_view(request, id = None):
    notices = None
    if id is not None:
        notices = Notice.objects.get(id = id)
    context = {
        "notice" : notices,
    }
    return render(request, "core/notice.html", context=context)


def merit_list_view(request, pk = None):
    merit_list = None
    if pk is not None:
        merit_list = MeritList.objects.get(id = pk)
    context = {
        "merit_list" : merit_list,
    }
    return render(request, "core/merit_list.html", context=context)



def about_view(request):
    our_vision = OurVision.objects.latest('id')
    principal = Principal.objects.latest('id')
    about = About.objects.latest('id')
    our_values = OurValues.objects.all()
    video = Video.objects.latest('id')
    former_principal = FormerPrincipal.objects.latest('id')

    context = {
        "our_vision" : our_vision,
        "principal" : principal,
        "about" : about,
        "our_values" : our_values,
        "video" : video,
        "former_principal" : former_principal,
    }
    return render(request, "core/about.html", context=context)
