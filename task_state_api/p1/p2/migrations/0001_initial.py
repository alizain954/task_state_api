# Generated by Django 4.0.4 on 2022-06-16 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(choices=[('draf', 'draf'), ('active', 'active'), ('done', 'done'), ('achieve', 'achieve')], default='draf', max_length=120)),
                ('title', models.CharField(max_length=120)),
            ],
        ),
    ]
