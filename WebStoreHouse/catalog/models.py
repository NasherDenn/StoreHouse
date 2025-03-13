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
        max_length=30,
        verbose_name="Тип оборудования",
        null=True,
        blank=True
    )

    manufacturer = models.CharField(
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

    first_id = models.CharField(
        max_length=5,
        verbose_name="ID",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.equipment_name


class WriteHistory(models.Model):
    date_write = models.DateField(
        null=True,
        blank=True,
    )

    time_write = models.TimeField(
        null=True,
        blank=True,
    )

    crud_write = models.CharField(
        max_length=15,
        verbose_name="Действие",
        null=True,
        blank=True,
        default=''
    )

    who_write = models.CharField(
        max_length=50,
        verbose_name="Кто",
        null=True,
        blank=True,
        default=''
    )

    from_write = models.CharField(
        max_length=50,
        verbose_name="Откуда",
        null=True,
        blank=True,
        default=''
    )

    whom_write = models.CharField(
        max_length=50,
        verbose_name="Кому",
        null=True,
        blank=True,
        default=''
    )

    to_write = models.CharField(
        max_length=50,
        verbose_name="Куда",
        null=True,
        blank=True,
        default=''
    )

    method_write = models.CharField(
        max_length=10,
        verbose_name="Метод",
        null=True,
        blank=True,
        default=''
    )

    manufacturer_write = models.CharField(
        max_length=50,
        verbose_name="Производитель",
        null=True,
        blank=True,
        default=''
    )

    type_write = models.CharField(
        max_length=50,
        verbose_name="Тип",
        null=True,
        blank=True,
        default=''
    )

    name_write = models.CharField(
        max_length=100,
        verbose_name="Название",
        null=True,
        blank=True,
        default=''
    )

    serial_number_write = models.CharField(
        max_length=30,
        verbose_name="Серийный номер",
        null=True,
        blank=True,
        default=''
    )

    total_write = models.CharField(
        max_length=30,
        verbose_name="Количество",
        null=True,
        blank=True,
    )

    location_write = models.CharField(
        max_length=20,
        verbose_name="Местонахождение",
        null=True,
        blank=True,
        default=''
    )

    status_write = models.CharField(
        max_length=20,
        verbose_name="Статус",
        null=True,
        blank=True,
        default=''
    )

    notes_write = models.CharField(
        max_length=200,
        verbose_name="Примечание",
        null=True,
        blank=True,
        default=''
    )

    id_write = models.IntegerField(
        verbose_name="ID",
        null=True,
        blank=True,
    )

    def __str__(self):
        return (f"{self.date_write} - {self.time_write} - {self.crud_write} - {self.who_write} - {self.from_write} "
                f"- {self.whom_write} - {self.to_write} - {self.method_write} - {self.manufacturer_write} - {self.type_write} "
                f"- {self.name_write} - {self.serial_number_write} - {self.total_write} - {self.location_write} - {self.status_write} "
                f"- {self.notes_write} - {self.id_write}")
