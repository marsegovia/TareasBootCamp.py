# Generated by Django 4.1.4 on 2022-12-27 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cine', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pelicula',
            name='Director',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Cine.director'),
        ),
    ]