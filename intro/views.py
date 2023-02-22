from django.contrib.auth.decorators import login_required

from django.http import HttpResponse
from django.shortcuts import render

@login_required()
def introduction(request):
    return HttpResponse('Hello')

@login_required()
def cars(request):
    context = {
        'all_cars': [
            {
                'brand': 'BMW',
                'color': 'Red',
                'year': 2022
            },
            {
                'brand': 'Dacia',
                'color': 'Blue',
                'year': 2021
            },
            {
                'brand': 'Audi',
                'color': 'Black',
                'year': 2020
            }
        ]
    }
    return render(request, 'intro/list_of_cars.html', context)

@login_required()
def books(request):
    context = {
        'all_books': [
            {
                'name': 'Surprise',
                'author': 'Danielle Steel',
                'type': 'SciFi',
                'year': 1999
            },
            {
                'name': 'Rebellion',
                'author': 'Kass Morgan',
                'type': 'SciFi',
                'year': 2021
            },
            {
                'name': 'Schi Love',
                'author': 'Margaret Smith',
                'type': 'Romance',
                'year': 1992
            },
            {
                'name': 'The House',
                'author': 'John Doe',
                'type': 'Drama',
                'year': 2003
            },
            {
                'name': 'Lost',
                'author': 'Jane Mile',
                'type': 'Horror',
                'year': 2017
            }
        ]
    }
    return render(request, 'intro/list_of_books.html', context)
