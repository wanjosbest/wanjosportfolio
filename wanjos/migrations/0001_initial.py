# Generated by Django 5.1.4 on 2024-12-05 22:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, null=True, unique=True)),
                ('name', models.CharField(max_length=100, null=True)),
                ('message', models.TextField(null=True)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='service_contact', to='wanjos.service')),
            ],
        ),
    ]
