from django.shortcuts import render, redirect

from django.views import generic

from .forms import *
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate

from .models import *


class UnitList(generic.ListView):
    model = Unit


class MethodList(generic.ListView):
    model = Unit.method


def login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth.login(request, user)
                # список значений для фильтров
                context_filter_method = MethodNdt.objects.all()
                context_filter_location = Location.objects.all()
                context_filter_status = Status.objects.all()
                # данные об оборудовании из БД
                unit_list = Unit.objects.all()
                return render(request, 'catalog/home.html', {
                    'context_filter_method': context_filter_method,
                    'context_filter_location': context_filter_location,
                    'context_filter_status': context_filter_status,
                    'unit_list': unit_list,
                })
        else:
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def filter(request):
    pass
