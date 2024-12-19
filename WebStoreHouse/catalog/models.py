from django.db import models


class MethodNdt(models.Model):
    name = models.CharField(
        max_length=5,
        help_text="Введите метод контроля",
        verbose_name="Метод контроля",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


# class Type(models.Model):
#     name = models.CharField(
#         max_length=30,
#         help_text="Введите тип оборудования",
#         verbose_name="Тип",
#         null=True,
#         blank=True
#     )
#
#     def __str__(self):
#         return self.name


# class Manufacturer(models.Model):
#     name = models.CharField(
#         max_length=50,
#         help_text="Введите производителя оборудования",
#         verbose_name="Производитель",
#         null=True,
#         blank=True
#     )
#
#     def __str__(self):
#         return self.name


class Status(models.Model):
    name = models.CharField(
        max_length=30,
        help_text="Введите статус оборудования",
        verbose_name="Статус оборудования",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(
        max_length=10,
        help_text="Введите месторасположение оборудования",
        verbose_name="Месторасположение"
    )

    def __str__(self):
        return self.name


class Unit(models.Model):
    method = models.ForeignKey(
        'MethodNdt',
        on_delete=models.CASCADE,
        help_text='Выберите метод контроля',
        verbose_name='Метод контроля',
        related_name='method'
    )

    type = models.CharField(
        # on_delete=models.CASCADE,
        max_length=30,
        verbose_name="Тип оборудования",
        null=True,
        blank=True
    )

    manufacturer = models.CharField(
        # on_delete=models.CASCADE,
        max_length=30,
        verbose_name="Производитель оборудования",
        null=True,
        blank=True
    )

    status = models.ForeignKey(
        'Status',
        on_delete=models.CASCADE,
        help_text='Выберите статус оборудования',
        verbose_name='Статус',
        related_name='status'
    )

    location = models.ForeignKey(
        'Location',
        on_delete=models.CASCADE,
        help_text='Выберите месторасположение оборудования',
        verbose_name='Месторасположение',
        related_name='location'
    )

    equipment_name = models.CharField(
        max_length=200,
        verbose_name="Название оборудования",
        # null=True,
        # blank=True
    )

    equipment_serial_number = models.CharField(
        max_length=50,
        verbose_name="Серийный номер",
        null=True,
        blank=True
    )

    total = models.IntegerField(
        verbose_name="Количество"
    )

    notes = models.CharField(
        max_length=200,
        verbose_name="Примечание",
        null=True,
        blank=True,
        default=''
    )

    def __str__(self):
        return self.equipment_name
