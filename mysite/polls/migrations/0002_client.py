# Generated by Django 4.2.1 on 2023-05-09 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=80)),
                ('created_at', models.CharField(max_length=27)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=64)),
                ('phone', models.CharField(max_length=20)),
                ('status', models.CharField(default='ACTIVE', max_length=20)),
            ],
        ),
    ]
