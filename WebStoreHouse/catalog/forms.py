from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput, MultiWidget
from django import forms
from .models import *
from .views import *


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


class UnitForm(forms.Form):
    method = forms.ModelChoiceField(label="Метод контроля", queryset=MethodNdt.objects, widget=forms.Select())
    # manufacturer = forms.ModelChoiceField(label="Производитель", queryset=Manufacturer.objects, widget=forms.Select())
    manufacturer = forms.CharField(label="Производитель", required=False)
    # type = forms.ModelChoiceField(label="Тип", queryset=Type.objects, widget=forms.Select())
    type = forms.CharField(label="Тип", required=False)
    name = forms.CharField(label="Название")
    serial = forms.CharField(label="Серийный номер", required=False)
    total = forms.IntegerField(label="Количество")
    location = forms.ModelChoiceField(label="Нахождение", queryset=Location.objects, widget=forms.Select())
    status = forms.CharField(label="Статус", required=False)
    # status = forms.ModelChoiceField(label="Статус", queryset=Status.objects, widget=forms.Select())
    notes = forms.CharField(label="Примечание", required=False)
    id = forms.CharField(label='id')
    id.widget = id.hidden_widget()


class EditForm(forms.Form):
    method = forms.ModelChoiceField(label="Метод контроля", queryset=MethodNdt.objects, widget=forms.Select())
    # manufacturer = forms.ModelChoiceField(label="Производитель", queryset=Manufacturer.objects, widget=forms.Select())
    manufacturer = forms.CharField(label="Производитель", required=False)
    # type = forms.ModelChoiceField(label="Тип", queryset=Type.objects, widget=forms.Select())
    type = forms.CharField(label="Тип", required=False)
    name = forms.CharField(label="Название")
    serial = forms.CharField(label="Серийный номер", required=False)
    total = forms.IntegerField(label="Количество")
    location = forms.ModelChoiceField(label="Нахождение", queryset=Location.objects, widget=forms.Select())
    status = forms.CharField(label="Статус", required=False)
    # status = forms.ModelChoiceField(label="Статус", queryset=Status.objects, widget=forms.Select())
    notes = forms.CharField(label="Примечание", required=False)
    id = forms.IntegerField(label='id')
    id.widget = id.hidden_widget()


class DeleteForm(forms.Form):
    name = forms.CharField(label="Вы действительно хотите удалить данное оборудование из базы данных?", disabled=True)
    serial = forms.CharField(label="Серийный номер", disabled=True)
    id = forms.IntegerField(label='id', disabled=True)


