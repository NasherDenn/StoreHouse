# Generated by Django 4.2.13 on 2024-07-03 09:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите производителя оборудования', max_length=50, verbose_name='Производитель')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите тип оборудования', max_length=30, verbose_name='Тип')),
            ],
        ),
        migrations.RemoveField(
            model_name='unit',
            name='equipment_manufacturer',
        ),
        migrations.RemoveField(
            model_name='unit',
            name='equipment_type',
        ),
        migrations.AddField(
            model_name='unit',
            name='manufacturer',
            field=models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.manufacturer', verbose_name='Производитель оборудования'),
        ),
        migrations.AddField(
            model_name='unit',
            name='type',
            field=models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.type', verbose_name='Тип оборудования'),
        ),
    ]
