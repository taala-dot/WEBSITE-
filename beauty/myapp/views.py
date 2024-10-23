# myapp/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import UserRegisterForm
from .models import HomePage,AboutUs,Testimonials

def index(request):
    first_slide = HomePage.objects.first()
    about_us = AboutUs.objects.first()
    testimonials = Testimonials.objects.all()

    context = {
        'first_slide': first_slide,
        'about_us': about_us,
        'testimonials': testimonials,
    }

    return render(request, 'index.html', context)
def lk_view(request):
    return render(request, 'lk.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Ваш аккаунт был создан! Вы вошли как {user.username}')
            return redirect('index')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})
