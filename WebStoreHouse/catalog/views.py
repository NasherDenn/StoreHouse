import json

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from .models import *
from django.views import generic
from .forms import *

from urllib import parse


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
                return redirect('/home')
        else:
            return render(request, 'registration/login.html', {'form': form})
    else:
        form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})


def home(request):
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


def unit_add(request):
    unit_form = UnitForm()
    return render(request, "catalog/unit_add.html", {"form": unit_form})


def create(request):
    if request.method == "POST":
        unit = Unit()
        # выбираем из экземпляра значение по выбранному значению по id
        method = MethodNdt.objects.get(id=request.POST.get("method"))
        unit.method = method
        manufacture = Manufacturer.objects.get(id=request.POST.get("manufacture"))
        unit.manufacturer = manufacture
        type = Type.objects.get(id=request.POST.get("type"))
        unit.type = type
        unit.equipment_name = request.POST.get("name")
        unit.equipment_serial_number = request.POST.get("serial")
        unit.total = request.POST.get("total")
        location = Location.objects.get(id=request.POST.get("location"))
        unit.location = location
        status = Status.objects.get(id=request.POST.get("status"))
        unit.status = status
        unit.notes = request.POST.get("notes")
        unit.save()
        return HttpResponseRedirect("/unit_add/")


def choice_unit_edit(request):
    context_filter_method = MethodNdt.objects.all()
    context_filter_location = Location.objects.all()
    context_filter_status = Status.objects.all()
    unit_list = Unit.objects.all()
    # return render(request, "catalog/choice_unit_edit.html", {'unit_list': unit_list})
    return render(request, 'catalog/choice_unit_edit.html', {
        'context_filter_method': context_filter_method,
        'context_filter_location': context_filter_location,
        'context_filter_status': context_filter_status,
        'unit_list': unit_list,
    })


def unit_edit(request, id):
    unit = Unit.objects.get(id=id)
    edit_form = EditForm(initial={
        'method': unit.method,
        'manufacture': unit.manufacturer,
        'type': unit.type,
        'name': unit.equipment_name,
        'serial': unit.equipment_serial_number,
        'total': unit.total,
        'location': unit.location,
        'status': unit.status,
        'notes': unit.notes,
        'id': id,
    })
    return render(request, "catalog/unit_edit.html", {"form": edit_form})


def unit_update(request):
    if request.method == "POST":
        id = request.POST.get("id")
        unit = Unit.objects.get(id=id)
        # выбираем из экземпляра значение по выбранному значению по id
        unit.method = MethodNdt.objects.get(id=id)
        method = MethodNdt.objects.get(id=request.POST.get("method"))
        unit.method = method
        manufacture = Manufacturer.objects.get(id=request.POST.get("manufacture"))
        unit.manufacturer = manufacture
        type = Type.objects.get(id=request.POST.get("type"))
        unit.type = type
        unit.equipment_name = request.POST.get("name")
        unit.equipment_serial_number = request.POST.get("serial")
        unit.total = request.POST.get("total")
        location = Location.objects.get(id=request.POST.get("location"))
        unit.location = location
        status = Status.objects.get(id=request.POST.get("status"))
        unit.status = status
        unit.notes = request.POST.get("notes")
        unit.save()
        return HttpResponseRedirect("/choice_unit_edit/")


def choice_unit_delete(request):
    context_filter_method = MethodNdt.objects.all()
    context_filter_location = Location.objects.all()
    context_filter_status = Status.objects.all()
    unit_list = Unit.objects.all()
    return render(request, 'catalog/choice_unit_delete.html', {
        'context_filter_method': context_filter_method,
        'context_filter_location': context_filter_location,
        'context_filter_status': context_filter_status,
        'unit_list': unit_list,
    })


def unit_delete(request, id):
    delete_form = DeleteForm(initial={'id': id})
    return render(request, "catalog/unit_delete.html", {'form_del': delete_form})


def unit_del(request):
    if request.method == "POST":
        id = request.POST.get("id")
        unit = Unit.objects.get(id=id)
        unit.delete()

        context_filter_method = MethodNdt.objects.all()
        context_filter_location = Location.objects.all()
        context_filter_status = Status.objects.all()
        unit_list = Unit.objects.all()
        return render(request, 'catalog/choice_unit_delete.html', {
            'context_filter_method': context_filter_method,
            'context_filter_location': context_filter_location,
            'context_filter_status': context_filter_status,
            'unit_list': unit_list,
        })


def unit_send(request):
    pass
