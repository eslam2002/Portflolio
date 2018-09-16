from django.shortcuts import render
from django.views.generic import CreateView
# from .forms import MassegeForm

def portfolio_home(request):
    return render(request,'portfolio_app/home.html',{})

# class MassegeCreateView(CreateView):
#     form_class = MassegeForm
#     template_name = 'portfolio_app/email_form.html'
#     success_url = '/'
#     contex_objecte_name = 'form'
