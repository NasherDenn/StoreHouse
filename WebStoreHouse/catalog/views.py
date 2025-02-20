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
    queryset = Unit.objects.all()
    unit = {}
    names = Location.objects.values_list('name', flat=True)
    loc = list(names)
    for index, i in enumerate(queryset):
        unit[index] = {'id': i.id, 'name': i.equipment_name, 'serial': i.equipment_serial_number, 'total': i.total, 'type': i.type,
                       'manufacturer': i.manufacturer, 'location': loc}
    data = json.dumps(unit)
    return render(request, "catalog/forms_send.html", {'data': data})


import logging

logger = logging.getLogger(__name__)  # Логирование

from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from openpyxl.drawing.image import Image
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, Border, Side, numbers
from openpyxl.worksheet.page import PageMargins
import io
import os
import datetime
from django.conf import settings
import warnings



@csrf_exempt  # Отключение CSRF для упрощения (не используйте в production)
def send_excel(request):
    if request.method == 'POST':
        try:
            raw_body = request.body.decode('utf-8')
            data = json.loads(raw_body)
            # Извлекаем данные
            table_data = data.get('data', [])
            # logger.error(table_data)



            # создаём файл Excel
            wb = Workbook()
            ws = wb.active
            ws.title = "Form Data"



            # вписать лист в одну страницу
            ws.page_setup.fitToPage = True
            ws.page_setup.paperSize = ws.PAPERSIZE_A4
            # Масштабирование по ширине (1 страница в ширину)
            ws.page_setup.fitToWidth = 1
            # Не ограничивать количество страниц по высоте
            ws.page_setup.fitToHeight = 0
            # чёрный стиль для границы
            thin = Side(border_style="thin", color="000000")
            medium = Side(border_style="medium", color="000000")

            # вставка изображение и адрес в зависимости от выбранного департамента
            if table_data[-1]['departament'] == 'YKR':
                img = Image(os.path.join(settings.BASE_DIR, 'catalog', 'static', 'images', 'Rutledge.png'))
                ws.add_image(img, 'C3')
                ws['E3'] = '      Yeskert Kyzmet Rutledge LLP,'
                ws['E3'].font = Font(name='Times New Roman', size=9)
                ws['E4'] = '      Atyrau, Republic of Kazakhstan,'
                ws['E4'].font = Font(name='Times New Roman', size=9)
                ws['E5'] = '      NDT department'
                ws['E5'].font = Font(name='Times New Roman', size=9)
            if table_data[-1]['departament'] == 'Arise':
                img = Image(os.path.join(settings.BASE_DIR, 'catalog', 'static', 'images', 'Arise.png'))
                ws.add_image(img, 'C3')
                ws['E3'] = '      Arise Kazakhstan LLP,'
                ws['E3'].font = Font(name='Times New Roman', size=9)
                ws['E4'] = '      Atyrau, Republic of Kazakhstan,'
                ws['E4'].font = Font(name='Times New Roman', size=9)
                ws['E5'] = '      NDT department'
                ws['E5'].font = Font(name='Times New Roman', size=9)
            # logger.error(table_data[-1]['departament'])
            # logger.error(table_data[-1]['recipient'])

            # шапка листа с форматированием
            ws['F3'] = 'Date:'
            ws['F3'].alignment = Alignment(horizontal='right')
            ws['F3'].font = Font(name='Times New Roman', size=11, bold=True)
            ws['F4'] = 'Time:'
            ws['F4'].alignment = Alignment(horizontal='right')
            ws['F4'].font = Font(name='Times New Roman', size=11, bold=True)
            ws['G3'] = f'{datetime.datetime.now():%A, %d %B %Y}'
            ws['G3'].font = Font(name='Times New Roman', size=9, underline='single')
            ws['G4'] = f'{datetime.datetime.now().time():%H:%M}'
            ws['G4'].font = Font(name='Times New Roman', size=9, underline='single')
            ws['E8'] = 'EQUIPMENT TRANSFER AGREEMENT'
            ws['E8'].alignment = Alignment(horizontal='center')
            ws['E8'].font = Font(name='Times New Roman', size=11, bold=True)
            ws['E9'] = 'Акт приема-передачи оборудования'
            ws['E9'].alignment = Alignment(horizontal='center')
            ws['E9'].font = Font(name='Times New Roman', size=11)
            # объединяем две ячейки для "№"
            ws.merge_cells(start_row=12, start_column=2, end_row=13, end_column=2)
            # заголовки таблицы на английском с форматированием
            ws['B12'] = '№'
            ws['B12'].alignment = Alignment(horizontal='center', vertical='center')
            ws['B12'].font = Font(name='Times New Roman', size=11, bold=True)
            ws['C12'] = 'Type'
            ws['C12'].alignment = Alignment(horizontal='center')
            ws['C12'].font = Font(name='Times New Roman', size=11, bold=True)
            ws['D12'] = 'Manufacture'
            ws['D12'].alignment = Alignment(horizontal='center')
            ws['D12'].font = Font(name='Times New Roman', size=11, bold=True)
            ws['E12'] = 'Name'
            ws['E12'].alignment = Alignment(horizontal='center')
            ws['E12'].font = Font(name='Times New Roman', size=11, bold=True)
            ws['F12'] = 'Serial Number'
            ws['F12'].alignment = Alignment(horizontal='center')
            ws['F12'].font = Font(name='Times New Roman', size=11, bold=True)
            ws['G12'] = 'Quantity'
            ws['G12'].alignment = Alignment(horizontal='center')
            ws['G12'].font = Font(name='Times New Roman', size=11, bold=True)
            # заголовки таблицы на русском с форматированием
            ws['B13'].alignment = Alignment(horizontal='center')
            ws['C13'] = 'Тип'
            ws['C13'].alignment = Alignment(horizontal='center')
            ws['C13'].font = Font(name='Times New Roman', size=11)
            ws['D13'] = 'Производитель'
            ws['D13'].alignment = Alignment(horizontal='center')
            ws['D13'].font = Font(name='Times New Roman', size=11)
            ws['E13'] = 'Наименование'
            ws['E13'].alignment = Alignment(horizontal='center')
            ws['E13'].font = Font(name='Times New Roman', size=11)
            ws['F13'] = 'Серийный номер'
            ws['F13'].alignment = Alignment(horizontal='center')
            ws['F13'].font = Font(name='Times New Roman', size=11)
            ws['G13'] = 'Кол-во'
            ws['G13'].alignment = Alignment(horizontal='center')
            ws['G13'].font = Font(name='Times New Roman', size=11)
            # высота первой строки
            ws.row_dimensions[1].height = 5.40
            # ширина столбцов
            ws.column_dimensions['A'].width = 2.33
            ws.column_dimensions['B'].width = 3.67
            ws.column_dimensions['C'].width = 14.67
            ws.column_dimensions['D'].width = 14.89
            ws.column_dimensions['E'].width = 48.78
            ws.column_dimensions['F'].width = 16.89
            ws.column_dimensions['G'].width = 10.22
            ws.column_dimensions['H'].width = 11.78
            # последняя строка основных данных таблицы
            last_index = 0
            # общее количество оборудования для отправки
            last_count_send_equipment = 0
            # основные данные таблицы
            for index, item in enumerate(table_data):
                if not len(item) == 2:
                    ws.row_dimensions[14 + index].height = 24.60
                    ws[f'B{14 + index}'] = int(item['index'])
                    ws[f'B{14 + index}'].number_format = numbers.FORMAT_NUMBER
                    ws[f'B{14 + index}'].border = Border(top=thin, bottom=thin, left=medium, right=thin)
                    ws[f'C{14 + index}'] = item['type']
                    ws[f'C{14 + index}'].border = Border(top=thin, bottom=thin, left=thin, right=thin)
                    ws[f'D{14 + index}'] = item['manufacturer']
                    ws[f'D{14 + index}'].border = Border(top=thin, bottom=thin, left=thin, right=thin)
                    ws[f'E{14 + index}'] = item['name']
                    ws[f'E{14 + index}'].border = Border(top=thin, bottom=thin, left=thin, right=thin)
                    ws[f'F{14 + index}'] = item['serial']
                    ws[f'F{14 + index}'].border = Border(top=thin, bottom=thin, left=thin, right=thin)
                    ws[f'G{14 + index}'] = int(item['count'])
                    ws[f'G{14 + index}'].border = Border(top=thin, bottom=thin, left=thin, right=medium)
                    last_count_send_equipment += int(item['count'])
                    # форматирование основных данных
                    ws[f'B{14 + index}'].alignment = Alignment(horizontal='center', vertical='center')
                    ws[f'B{14 + index}'].font = Font(name='Bahnschrift SemiLight', size=10)
                    ws[f'C{14 + index}'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
                    ws[f'C{14 + index}'].font = Font(name='Bahnschrift SemiLight', size=10)
                    ws[f'D{14 + index}'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
                    ws[f'D{14 + index}'].font = Font(name='Bahnschrift SemiLight', size=10)
                    ws[f'E{14 + index}'].alignment = Alignment(horizontal='center', vertical='center', wrap_text=True)
                    ws[f'E{14 + index}'].font = Font(name='Bahnschrift SemiLight', size=10)
                    ws[f'F{14 + index}'].alignment = Alignment(horizontal='center', vertical='center')
                    ws[f'F{14 + index}'].font = Font(name='Bahnschrift SemiLightn', size=10)
                    ws[f'G{14 + index}'].alignment = Alignment(horizontal='center', vertical='center')
                    ws[f'G{14 + index}'].font = Font(name='Bahnschrift SemiLight', size=10)
                last_index = 14 + index
            # граница шапки таблицы
            ws[f'B12'].border = Border(top=medium, bottom=medium, left=medium)
            ws[f'B13'].border = Border(top=medium, bottom=medium, left=medium)
            ws[f'C12'].border = Border(top=medium, left=thin, right=thin)
            ws[f'C13'].border = Border(bottom=medium, left=thin, right=thin)
            ws[f'D12'].border = Border(top=medium, left=thin, right=thin)
            ws[f'D13'].border = Border(bottom=medium, left=thin, right=thin)
            ws[f'E12'].border = Border(top=medium, left=thin, right=thin)
            ws[f'E13'].border = Border(bottom=medium, left=thin, right=thin)
            ws[f'F12'].border = Border(top=medium, left=thin, right=thin)
            ws[f'F13'].border = Border(bottom=medium, left=thin, right=thin)
            ws[f'G12'].border = Border(top=medium, left=thin, right=medium)
            ws[f'G13'].border = Border(bottom=medium, left=thin, right=medium)
            # граница футера таблицы
            ws[f'B{last_index}'].border = Border(top=medium)
            ws[f'C{last_index}'].border = Border(top=medium)
            ws[f'D{last_index}'].border = Border(top=medium)
            ws[f'E{last_index}'].border = Border(top=medium)
            ws[f'F{last_index}'].border = Border(top=medium)
            ws[f'G{last_index}'].border = Border(top=medium)

            # logger.error(type(last_index))
            # футер листа с форматированием
            # высота первой строки
            ws.row_dimensions[last_index].height = 27
            ws[f'G{int(last_index)}'] = last_count_send_equipment
            ws[f'G{int(last_index)}'].alignment = Alignment(horizontal='center', vertical='center')
            ws[f'G{int(last_index)}'].font = Font(name='Times New Roman', size=11)
            ws[f'G{int(last_index)}'].border = Border(top=medium, bottom=medium, left=medium, right=medium)

            ws.merge_cells(start_row=int(last_index) + 2, start_column=2, end_row=int(last_index) + 2, end_column=3)
            ws[f'B{int(last_index) + 2}'] = 'Handed out:'
            ws[f'B{int(last_index) + 2}'].font = Font(name='Times New Roman', size=11, bold=True)

            ws.merge_cells(start_row=int(last_index) + 3, start_column=2, end_row=int(last_index) + 3, end_column=3)
            ws[f'B{int(last_index) + 3}'] = 'Сдал'
            ws[f'B{int(last_index) + 3}'].font = Font(name='Times New Roman', size=11)

            ws.merge_cells(start_row=int(last_index) + 5, start_column=2, end_row=int(last_index) + 5, end_column=3)
            ws[f'B{int(last_index) + 5}'] = 'Sign (подпись)'
            ws[f'B{int(last_index) + 5}'].alignment = Alignment(horizontal='center')
            ws[f'B{int(last_index) + 5}'].font = Font(name='Times New Roman', size=8)
            # thin = Side(border_style="thin", color="000000")
            ws[f'B{int(last_index) + 5}'].border = Border(top=thin)
            ws[f'C{int(last_index) + 5}'].border = Border(top=thin)

            ws.merge_cells(start_row=int(last_index) + 5, start_column=4, end_row=int(last_index) + 5, end_column=5)
            ws[f'D{int(last_index) + 5}'] = 'Full name (расшифровка подписи)'
            ws[f'D{int(last_index) + 5}'].alignment = Alignment(horizontal='center')
            ws[f'D{int(last_index) + 5}'].font = Font(name='Times New Roman', size=8)
            ws[f'D{int(last_index) + 5}'].border = Border(top=thin)
            ws[f'E{int(last_index) + 5}'].border = Border(top=thin)

            ws.merge_cells(start_row=int(last_index) + 7, start_column=2, end_row=int(last_index) + 7, end_column=3)
            ws[f'B{int(last_index) + 7}'] = 'Received: '
            ws[f'B{int(last_index) + 7}'].font = Font(name='Times New Roman', size=11, bold=True)

            ws.merge_cells(start_row=int(last_index) + 8, start_column=2, end_row=int(last_index) + 8, end_column=3)
            ws[f'B{int(last_index) + 8}'] = 'Принял'
            ws[f'B{int(last_index) + 8}'].font = Font(name='Times New Roman', size=11)

            ws.merge_cells(start_row=int(last_index) + 10, start_column=2, end_row=int(last_index) + 10, end_column=3)
            ws[f'B{int(last_index) + 10}'] = 'Sign (подпись)'
            ws[f'B{int(last_index) + 10}'].alignment = Alignment(horizontal='center')
            ws[f'B{int(last_index) + 10}'].font = Font(name='Times New Roman', size=8)

            ws[f'B{int(last_index) + 10}'].border = Border(top=thin)
            ws[f'C{int(last_index) + 10}'].border = Border(top=thin)

            ws.merge_cells(start_row=int(last_index) + 10, start_column=4, end_row=int(last_index) + 10, end_column=5)
            ws[f'D{int(last_index) + 10}'] = 'Full name (расшифровка подписи)'
            ws[f'D{int(last_index) + 10}'].alignment = Alignment(horizontal='center')
            ws[f'D{int(last_index) + 10}'].font = Font(name='Times New Roman', size=8)
            ws[f'D{int(last_index) + 10}'].border = Border(top=thin)
            ws[f'E{int(last_index) + 10}'].border = Border(top=thin)

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
