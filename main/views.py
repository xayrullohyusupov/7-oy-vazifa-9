from django.shortcuts import render
from . import models

def index(request):
    items = models.ChooseItem.objects.all()
    members = models.TeamMember.objects.all()
    partners = models.Partner.objects.all()
    context = {
        'items': items,
        'members': members,
        'partners': partners,
    }
        
    return render(request, 'front/index.html', context)

    
