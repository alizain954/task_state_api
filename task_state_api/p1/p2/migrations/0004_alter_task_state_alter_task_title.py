# Generated by Django 4.0.4 on 2022-06-16 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p2', '0003_task_delete_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='state',
            field=models.CharField(choices=[('draft', 'draft'), ('active', 'active'), ('done', 'done'), ('archived', 'archived')], max_length=8),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
