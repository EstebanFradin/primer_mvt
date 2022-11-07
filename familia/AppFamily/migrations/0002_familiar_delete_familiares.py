# Generated by Django 4.1.3 on 2022-11-07 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppFamily', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido', models.CharField(max_length=40)),
                ('numero', models.IntegerField()),
                ('fecha', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='familiares',
        ),
    ]
