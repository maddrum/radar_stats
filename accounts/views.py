from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from accounts import forms


# Create your views here.
class UserRegisterView(CreateView):
    form_class = forms.AccountRegisterForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


class ThankYouView(TemplateView):
    template_name = 'accounts/logout.html'



class UserProfileMainView(TemplateView):
    pass
