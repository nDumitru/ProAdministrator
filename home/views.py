from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView

from management.models import Aministrator


class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'  # specificam calea catre pagin .html pentru aceasta clasa


def search(request):
    search = request.GET.get('search')
    if search:
        all_entries = Aministrator.objects.filter(
            Q(course__icontains=search) | Q(first_name__icontains=search))  # cu si & iar cu not cu exclude
    else:
        all_entries = Aministrator.objects.all()

    return render(request, 'templates/search.html', {'entries': all_entries})
