from django.db.models import Q
from django.shortcuts import render
from .models import Resident

def search_residents(request):
    if request.method == 'POST':
        search_query = request.POST['search_query']
        residents = Resident.objects.filter(
            Q(name__icontains=search_query) |
            Q(apartment_number__icontains=search_query)
        )
        context = {
            'residents': residents,
            'search_query': search_query
        }
        return render(request, 'residents/search_results.html', context)
    else:
        return render(request, 'residents/search_residents.html')
