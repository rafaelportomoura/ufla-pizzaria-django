# Generated by Django 4.2.1 on 2023-05-10 00:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0008_remove_group_employees_remove_group_paths_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='status',
            field=models.IntegerField(choices=[(0, 'INACTIVE'), (1, 'ACTIVE')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.IntegerField(choices=[(0, 'Lacking'), (1, 'Available')], default=1),
        ),
    ]