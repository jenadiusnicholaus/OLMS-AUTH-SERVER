# Generated by Django 4.1.1 on 2022-10-11 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmployerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employer_name', models.CharField(max_length=100, unique=True)),
                ('tin', models.CharField(max_length=100)),
                ('short_code', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': ('Employer',),
                'verbose_name_plural': 'Employers',
            },
        ),
    ]
