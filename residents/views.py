from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from residents.filters import ResidentFilter
from .forms import ResidentForm, ResidentUpdateForm
from .models import Resident


class ResidentCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = '../templates/residents/add_resident.html'
    model = Resident
    form_class = ResidentForm
    success_url = reverse_lazy('list-of-residents')


class ResidentListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    template_name = '../templates/residents/list_of_residents.html'
    model = Resident
    context_object_name = 'all_residents'
    permission_required = 'residents.view_resident'

    def get_queryset(self):
        return Resident.objects.filter(active=True)
        #  (is_olympic=True,  )

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        residents = Resident.objects.filter(active=True)
        filters = ResidentFilter(self.request.GET, queryset=residents)
        residents = filters.qs

        data['all_residents'] = residents
        data['my_filters'] = filters

        return data


class ResidentUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    template_name = '../templates/residents/update_resident.html'
    model = Resident
    form_class = ResidentUpdateForm
    success_url = reverse_lazy('list-of-residents')
    permission_required = 'residents.change_resident'


class ResidentDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    template_name = '../templates/residents/delete_resident.html'
    model = Resident
    success_url = reverse_lazy('list-of-residents')
    permission_required = 'residents.delete_resident'


class ResidentDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    template_name = '../templates/residents/details_of_resident.html'
    model = Resident
    permission_required = 'residents.view_resident'


@login_required()
@permission_required('residents.inactive_resident')
def inactivate_resident(request, pk):
    #  Resident.objects.filter(id=pk).delete() # sterg residentul cu id(pk) din tabela resident_resident
    Resident.objects.filter(id=pk).update(active=False)
    #  se pune ,daca se doreste sa se actualizeze mai multe coloane
    return redirect('list-of-residents')
