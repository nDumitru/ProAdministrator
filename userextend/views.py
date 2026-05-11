import random

from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.models import ProAdminUser
from userextend.forms import UserExtendForm


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = ProAdminUser
    form_class = UserExtendForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_user = form.save(commit=False)
            new_user.first_name = new_user.first_name.title()
            new_user.save()

            new_user.is_active = False

            details_user = {
                'fullname': f'{new_user.first_name} {new_user.last_name}',
                'email': new_user.email,
                'url': f'http://127.0.0.1:8000/confirm/{new_user.id}/'
            }
            subject = f'Ti-ai creat un cont nou'
            message = get_template('mail.html').render(details_user)

            mail = EmailMessage(subject, message, settings.EMAIL_HOST_USER, [new_user.email])
            mail.content_subtype = 'html'
            mail.send()

        return redirect('login')

def confirm_account(request, pk):
    ProAdminUser.objects.filter(id=pk).update(is_active=True)
    return redirect('login')