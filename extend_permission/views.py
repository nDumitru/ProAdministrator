from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views import generic
from django.shortcuts import render
from django.db.models import Q
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin
from forms import ExtendUserForm, ExtendPermissionForm
from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from forms import ExtendUserForm
from models import Permission, ExtendPermission


User = get_user_model()
# View for rendering user information
@login_required
def UserDetailView(request, pk):
    user = User.objects.get(pk=pk)
    permission = Permission.objects.get(user=user)
    return render(request, 'extend_permission/user_detail.html', {'user': user, 'permission': permission})

# View for extending user permission
@login_required
def ExtendUserPermission(request, pk):
    user = User.objects.get(pk=pk)
    permission = Permission.objects.get(user=user)
    if request.method == 'POST':
        form = ExtendUserForm(request.POST, instance=permission)
        if form.is_valid():
            form.save()
    else:
        form = ExtendUserForm(instance=permission)
    return render(request, 'extend_permission/permission_form.html', {'form': form, 'user': user})

# View for creating a user
class SignUpView(SuccessMessageMixin, CreateView):
    template_name = 'registration/signup.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    success_message = 'Your account was created successfully'

# View for updating a user's information
class UserUpdateView(SuccessMessageMixin, UpdateView):
    model = User
    form_class = ExtendUserForm
    template_name = 'extend_permission/user_form.html'
    success_url = reverse_lazy('home')
    success_message = 'Your profile was updated successfully'

# View for deleting a user
class UserDeleteView(SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'extend_permission/user_confirm_delete.html'
    success_url = reverse_lazy('home')
    success_message = 'Your account was deleted successfully'

# View for rendering all users and their information
class UserListView(generic.ListView):
    model = User
    template_name = 'extend_permission/user_list.html'

# View for rendering all groups and their information
class GroupListView(generic.ListView):
    model = Group
    template_name = 'extend_permission/group_list.html'

class ExtendUserView(LoginRequiredMixin, CreateView):
    model = User
    form_class = ExtendUserForm
    template_name = 'extend_permission/user.html'
    success_url = reverse_lazy('users')

class ExtendPermissionView(LoginRequiredMixin, ListView):
    model = User
    template_name = 'extend_permission/permissions.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            queryset = User.objects.filter(
                Q(username__icontains=query) | Q(first_name__icontains=query) | Q(last_name__icontains=query)
            ).distinct()
        else:
            queryset = User.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ExtendPermissionForm()
        return context

    def post(self, request, *args, **kwargs):
        form = ExtendPermissionForm(request.POST)
        if form.is_valid():
            user = User.objects.get(id=form.cleaned_data['user'])
            permission = form.cleaned_data['permission']
            user.user_permissions.add(permission)
        return render(request, self.template_name, {'form': form, 'object_list': self.get_queryset()})


class ExtendPermissionListView(ListView):
    model = ExtendPermission
    template_name = 'extend_permission/extend_permission_list.html'
    context_object_name = 'permissions'

class ExtendPermissionCreateView(CreateView):
    model = ExtendPermission
    fields = '__all__'
    template_name = 'extend_permission/extend_permission_form.html'
    success_url = reverse_lazy('extend_permission:extend_permission_list')

class ExtendPermissionUpdateView(UpdateView):
    model = ExtendPermission
    fields = '__all__'
    template_name = 'extend_permission/extend_permission_form.html'
    success_url = reverse_lazy('extend_permission:extend_permission_list')

class ExtendPermissionDeleteView(DeleteView):
    model = ExtendPermission
    template_name = 'extend_permission/extend_permission_confirm_delete.html'
    success_url = reverse_lazy('extend_permission:extend_permission_list')
