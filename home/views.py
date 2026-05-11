from django.db.models import Q
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from management.models import Administrator


@method_decorator(login_required, name='dispatch')
class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            from management.models import Block, Apartment, Resident
            context['blocks'] = Block.objects.count()
            context['apartments'] = Apartment.objects.count()
            context['residents'] = Resident.objects.filter(active=True).count()
            context['administrators'] = Administrator.objects.filter(is_active=True).count()
        except Exception:
            context['blocks'] = 0
            context['apartments'] = 0
            context['residents'] = 0
            context['administrators'] = 0
        return context


def search(request):
    search = request.GET.get('search')
    if search:
        all_entries = Administrator.objects.filter(
            Q(first_name__icontains=search) | Q(last_name__icontains=search) | Q(email__icontains=search)
        )
    else:
        all_entries = Administrator.objects.all()[:10]

    return render(request, 'search.html', {'entries': all_entries})