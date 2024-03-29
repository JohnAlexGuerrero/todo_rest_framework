# Generated by Django 5.0 on 2024-01-02 02:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task', models.CharField(max_length=180, verbose_name='tarea')),
                ('timestamp', models.DateTimeField(auto_now_add=True, verbose_name='creacion')),
                ('completed', models.BooleanField(blank=True, default=False, verbose_name='completo')),
                ('updated', models.DateTimeField(blank=True, verbose_name='actualizacion')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='users')),
            ],
            options={
                'verbose_name': 'Todo',
                'verbose_name_plural': 'Todos',
            },
        ),
    ]
