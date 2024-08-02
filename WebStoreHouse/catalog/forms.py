from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms
from .models import *
from .views import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class UnitForm(forms.Form):
    method = forms.ModelChoiceField(label="Метод контроля", queryset=MethodNdt.objects, widget=forms.Select())
    manufacture = forms.ModelChoiceField(label="Производитель", queryset=Manufacturer.objects, widget=forms.Select())
    type = forms.ModelChoiceField(label="Тип", queryset=Type.objects, widget=forms.Select())
    name = forms.CharField(label="Название")
    serial = forms.CharField(label="Серийный номер", required=False)
    total = forms.IntegerField(label="Количество")
    location = forms.ModelChoiceField(label="Нахождение", queryset=Location.objects, widget=forms.Select())
    status = forms.ModelChoiceField(label="Статус", queryset=Status.objects, widget=forms.Select())
    notes = forms.CharField(label="Примечание", required=False)


class EditForm(forms.Form):
    method = forms.ModelChoiceField(label="Метод контроля", queryset=MethodNdt.objects, widget=forms.Select())
    manufacture = forms.ModelChoiceField(label="Производитель", queryset=Manufacturer.objects, widget=forms.Select())
    type = forms.ModelChoiceField(label="Тип", queryset=Type.objects, widget=forms.Select())
    name = forms.CharField(label="Название")
    serial = forms.CharField(label="Серийный номер", required=False)
    total = forms.IntegerField(label="Количество")
    location = forms.ModelChoiceField(label="Нахождение", queryset=Location.objects, widget=forms.Select())
    status = forms.ModelChoiceField(label="Статус", queryset=Status.objects, widget=forms.Select())
    notes = forms.CharField(label="Примечание", required=False)
    id = forms.IntegerField(label='id')


class DeleteForm(forms.Form):
    id = forms.IntegerField(label='id')

