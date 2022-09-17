# Generated by Django 4.1 on 2022-09-17 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Platos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=55, verbose_name='nombre')),
                ('origen', models.CharField(max_length=255, verbose_name='origen')),
                ('precio', models.IntegerField(verbose_name='precio')),
            ],
        ),
    ]
