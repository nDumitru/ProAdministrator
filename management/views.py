from .forms import BlockForm, ApartmentForm, ResidentForm, ManagerForm
from .models import Block, Apartment, Resident, Manager
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from .models import Administrator
from .forms import AdministratorForm, AdministratorUpdateForm


class AdministratorCreateView(LoginRequiredMixin, CreateView):
    model = Administrator
    form_class = AdministratorForm
    template_name = 'management/create_administrator.html'
    success_url = reverse_lazy('list-of-administrators')

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class AdministratorListView(LoginRequiredMixin, ListView):
    model = Administrator
    context_object_name = 'administrators'
    template_name = 'management/list_of_administrators.html'


class AdministratorUpdateView(LoginRequiredMixin, UpdateView):
    model = Administrator
    form_class = AdministratorUpdateForm
    template_name = 'management/update_administrator.html'
    success_url = reverse_lazy('list-of-administrators')

    def form_valid(self, form):
        form.instance.updated_by = self.request.user
        return super().form_valid(form)


class AdministratorDeleteView(LoginRequiredMixin, DeleteView):
    model = Administrator
    success_url = reverse_lazy('list-of-administrators')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, 'Administrator was deleted successfully.')
        return super().delete(request, *args, **kwargs)


class AdministratorDetailView(LoginRequiredMixin, DetailView):
    model = Administrator
    template_name = '../templates/management/details_of_administrator.html'


@method_decorator(login_required, name='dispatch')
def inactivate_administrator(request, pk):
    admin = Administrator.objects.get(pk=pk)
    if request.method == 'POST':
        admin.is_active = False
        admin.save()
        messages.success(request, 'Administrator was inactivated successfully.')
        return redirect('list-of-administrators')
    return render(request, 'management/inactivate_administrator.html', {'admin': admin})


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
