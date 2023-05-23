# Generated by Django 4.2.1 on 2023-05-09 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(0, 'Cancelled'), (1, 'Placed'), (2, 'Processing'), (3, 'Completed')], default=1, max_length=2)),
                ('datetime', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='polls.client')),
                ('employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='polls.employee')),
            ],
        ),
    ]