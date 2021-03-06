# Generated by Django 4.0.4 on 2022-06-05 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=255, verbose_name='Адрес')),
            ],
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('ip_address', models.CharField(max_length=255, verbose_name='IP адрес')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printer.address')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='printer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='printer.printer'),
        ),
    ]
