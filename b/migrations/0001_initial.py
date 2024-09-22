# Generated by Django 5.1.1 on 2024-09-22 02:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('a', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='B',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dic_value', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('a', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a_db', to='a.a')),
            ],
        ),
    ]
