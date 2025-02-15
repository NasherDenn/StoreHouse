import json

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.urls import reverse_lazy
from django.views.generic import UpdateView
from django.core.serializers import serialize
from django.http import JsonResponse
from .models import *
from django.views import generic
from .forms import *
# import wadofstuff
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods

from openpyxl import Workbook


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
                return redirect('home/')
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
    unit_form = UnitForm()
    return render(request, 'catalog/home.html', {
        'context_filter_method': context_filter_method,
        'context_filter_location': context_filter_location,
        'context_filter_status': context_filter_status,
        'unit_list': unit_list,
        'form_add': unit_form,
    })


def create(request):
    if request.method == "POST":
        unit = Unit()
        # выбираем из экземпляра значение по выбранному значению по id
        method = MethodNdt.objects.get(id=request.POST.get("method"))
        unit.method = method
        # manufacture = Manufacturer.objects.get(id=request.POST.get("manufacture"))
        # unit.manufacturer = manufacture
        unit.manufacturer = request.POST.get("manufacturer")
        # type = Type.objects.get(id=request.POST.get("type"))
        # unit.type = type
        unit.type = request.POST.get("type")
        unit.equipment_name = request.POST.get("name")
        unit.equipment_serial_number = request.POST.get("serial")
        unit.total = request.POST.get("total")
        location = Location.objects.get(id=request.POST.get("location"))
        unit.location = location
        status = Status.objects.get(id=request.POST.get("status"))
        unit.status = status
        unit.notes = request.POST.get("notes")
        unit.save()
        return home(request)


def unit_edit(request, id):
    unit = Unit.objects.get(id=id)
    edit_form = EditForm(initial={
        'method': unit.method,
        'manufacturer': unit.manufacturer,
        'type': unit.type,
        'name': unit.equipment_name,
        'serial': unit.equipment_serial_number,
        'total': unit.total,
        'location': unit.location,
        'status': unit.status,
        'notes': unit.notes,
        'id': id,
    })
    return render(request, "catalog/unit_edit.html", {"form_edit": edit_form})


def unit_update(request):
    if request.method == "POST":
        id = request.POST.get("id")
        unit = Unit.objects.get(id=id)
        # выбираем из экземпляра значение по выбранному значению по id
        method = MethodNdt.objects.get(id=request.POST.get("method"))
        unit.method = method
        # manufacture = Manufacturer.objects.get(id=request.POST.get("manufacture"))
        # unit.manufacturer = manufacture
        unit.manufacturer = request.POST.get("manufacturer")
        # type = Type.objects.get(id=request.POST.get("type"))
        # unit.type = type
        unit.type = request.POST.get("type")
        unit.equipment_name = request.POST.get("name")
        unit.equipment_serial_number = request.POST.get("serial")
        unit.total = request.POST.get("total")
        location = Location.objects.get(id=request.POST.get("location"))
        unit.location = location
        status = Status.objects.get(id=request.POST.get("status"))
        unit.status = status
        unit.notes = request.POST.get("notes")
        unit.save()
        return HttpResponseRedirect("/home/")


def unit_delete(request, id):
    unit = Unit.objects.get(id=id)
    unit.delete()
    return HttpResponseRedirect('/home/')


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'


from django.core.serializers.json import DjangoJSONEncoder
import json


def forms_send(request):
    # if request.method == "POST":
    # param = request.POST.get('param')

    queryset = Unit.objects.all()
    unit = {}
    for index, i in enumerate(queryset):
        unit[index] = {'id': i.id, 'name': i.equipment_name, 'serial': i.equipment_serial_number, 'total': i.total, 'type': i.type,
                       'manufacturer': i.manufacturer, 'location': i.location.name}
    data = json.dumps(unit)
    return render(request, "catalog/forms_send.html", {'data': data})
    # return HttpResponse(data, content_type="application/json")


import logging

logger = logging.getLogger(__name__)  # Логирование

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from openpyxl import Workbook
import io


@csrf_exempt  # Отключение CSRF для упрощения (не используйте в production)
def send_excel(request):
    logger.error(f'0')
    if request.method == 'POST':
        logger.error(f'1')
        try:
            # # logger.error(f'2 {request.body}')
            # # Получение данных из запроса
            # data = json.loads(request.body)
            # logger.error(f'3 {data}')
            # cellVal = data.get('data', {})
            # logger.error(f'4 {cellVal}')

            floating_select = request.POST.get('floatingSelect')
            count_values = request.POST.getlist('count')  # Для полей с несколькими значениями
            logger.error(f'4 {floating_select}')
            logger.error(f'5 {count_values}')
            wb = Workbook()
            ws = wb.active
            ws.title = "Form Data"
            ws.append(["Floating Select", "Count"])
            ws.append([floating_select, ", ".join(count_values)])

            # Создание Excel-файла
            # wb = Workbook()
            # for sheet_name, rows in cellVal.items():
            #     ws = wb.create_sheet(title=sheet_name)
            #     for row in rows:
            #         ws.append(list(row.values()))

            # Удаление дефолтного листа (если нужно)
            # if 'Sheet' in wb.sheetnames:
            #     del wb['Sheet']

            # Сохранение файла в буфер
            buffer = io.BytesIO()
            wb.save(buffer)
            buffer.seek(0)

            # Возврат файла как ответ
            response = HttpResponse(buffer.read(), content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
            response['Content-Disposition'] = 'attachment; filename=output.xlsx'
            return response
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

# ToDo: forms_send.html - при нажатии на кнопку "Отправить" сформировать файл Excel с актом приёмо-передачи оборудования
    # ToDo: при отправке данных в django отправляется форма, а не json - только значения из input (столбец - количество)


# ToDo: изменить данные в БД (местонахождение, количество) при нажатии кнопки "Отправить" в forms_send.html
# ToDo: занести сведения в БД (история перемещения) об оборудовании (дата, данные оборудования, откуда-куда, кто отправил)
# ToDo: сделать БД с историей перемещения оборудования
# ToDo: сделать ссылку (на закладке "Главная") на оборудовании для просмотра истории перемещения (отдельно открывающаяся страница) оборудования
# ToDo: установить ограничения на действия для разных пользователей
# ToDo: неправильно работают фильтры: если выбран фильтр и ввести в HotSearch, то не учитывается основной фильтр, затем после очистки HotSearch
    # ToDo: основной фильтр не работает
