# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-17 03:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='state',
            unique_together=set([('name',)]),
        ),
        migrations.AddField(
            model_name='city',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_name', to='mainapp.State'),
        ),
        migrations.AlterUniqueTogether(
            name='city',
            unique_together=set([('name', 'state')]),
        ),
    ]
