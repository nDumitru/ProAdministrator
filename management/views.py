from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import BlockForm, ApartmentForm, ResidentForm, ManagerForm
from .models import Block, Apartment, Resident, Manager


@login_required
def index(request):
    blocks = Block.objects.all()
    apartments = Apartment.objects.all()
    residents = Resident.objects.all()
    managers = Manager.objects.all()

    context = {
        'blocks': blocks,
        'apartments': apartments,
        'residents': residents,
        'managers': managers
    }
    return render(request, '../templates/management/index.html', context)


@login_required
def add_block(request):
    if request.method == 'POST':
        form = BlockForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Block has been added successfully.')
            return redirect('management_index')
    else:
        form = BlockForm()

    context = {
        'form': form,
        'title': 'Add Block'
    }
    return render(request, 'management/form.html', context)


@login_required
def add_apartment(request):
    if request.method == 'POST':
        form = ApartmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Apartment has been added successfully.')
            return redirect('management_index')
    else:
        form = ApartmentForm()

    context = {
        'form': form,
        'title': 'Add Apartment'
    }
    return render(request, 'management/form.html', context)


@login_required
def add_resident(request):
    if request.method == 'POST':
        form = ResidentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Resident has been added successfully.')
            return redirect('management_index')
    else:
        form = ResidentForm()

    context = {
        'form': form,
        'title': 'Add Resident'
    }
    return render(request, 'management/form.html', context)


@login_required
def add_manager(request):
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Manager has been added successfully.')
            return redirect('management_index')
    else:
        form = ManagerForm()

    context = {
        'form': form,
        'title': 'Add Manager'
    }
    return render(request, 'management/form.html', context)


@login_required
def edit_block(request, block_id):
    block = Block.objects.get(pk=block_id)

    if request.method == 'POST':
        form = BlockForm(request.POST, instance=block)
        if form.is_valid():
            form.save()
            messages.success(request, 'Block has been updated successfully.')
            return redirect('management_index')
    else:
        form = BlockForm(instance=block)

    context = {
        'form': form,
        'title': 'Edit Block',
        'block_id': block_id
    }
    return render(request, 'management/form.html', context)


@login_required
def edit_apartment(request, apartment_id):
    apartment = Apartment.objects.get(pk=apartment_id)

    if request.method == 'POST':
        form = ApartmentForm(request.POST, instance=apartment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Apartment has been updated successfully.')
            return redirect('management_index')
    else:
        form = ApartmentForm(instance=apartment)

    context = {
        'form': form,
        'title': 'Edit Apartment',
        'apartment_id': apartment_id
    }
    return render(request, '../templates/management/form.html', context)
