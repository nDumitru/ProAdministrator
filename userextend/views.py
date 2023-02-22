import random

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, EmailMessage
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView

from ProAdmin.settings import EMAIL_HOST_USER
from userextend.forms import UserExtendForm


class UserCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = User
    form_class = UserExtendForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            new_user = form.save(commit=False) # comit=False - pastreaza datele dar nu le salveaza
            new_user.first_name = new_user.first_name.title() # sa inceapa titlul cu litera mare
            new_user.username = f'{new_user.first_name.lower()}{new_user.last_name.lower()}_{random.randint(100000, 999999)}'

            new_user.save()

            # Email fara template
            new_user.is_active = False

            # subject = 'Ti-ai creat un cont nou'
            # message = f'Hello, {new_user.first_name}' \
            #           f' {new_user.last_name} ti-ai creat cont in aplicatia mea cu username-ul : {new_user.username}'
            # send_mail(subject, message, EMAIL_HOST_USER, {new_user.email})


            # Email cu template
            details_user ={
                'fullname': f'{new_user.first_name} {new_user.last_name}',
                'username': f'{new_user.username}',
                'url': f'http://127.0.0.1:8000/confirm/{new_user.id}/'
            }
            subject = f'Ti-ai creat un cont nou'
            message = get_template('mail.html').render(details_user)

            mail = EmailMessage(subject, message, EMAIL_HOST_USER, [new_user.email])
            mail.content_subtype = 'html' # main content is now text/html
            mail.send()

        return redirect('login')

def confirm_account(request, pk):
    User.objects.filter(id=pk).update(is_active=True)
    return redirect('login')