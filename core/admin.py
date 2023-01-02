from django.contrib import admin
from .models import (
    About,
    CampusLife,
    FormerPrincipal,
    Notice,
    MeritList,
    Event,
    OurVision,
    Principal,
    Action,
    Header,
    OurValues,
    Video,
    News,
)

# Register your models here.
admin.site.register(Header)
admin.site.register(Notice)
admin.site.register(MeritList)
admin.site.register(Event)
admin.site.register(Principal)
admin.site.register(OurVision)
admin.site.register(About)
admin.site.register(Action)  
admin.site.register(OurValues) 
admin.site.register(Video) 
admin.site.register(FormerPrincipal) 
admin.site.register(CampusLife) 
admin.site.register(News) 
