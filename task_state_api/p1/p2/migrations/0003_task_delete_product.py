# Generated by Django 4.0.4 on 2022-06-16 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p2', '0002_alter_product_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=120)),
                ('title', models.CharField(max_length=120)),
            ],
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
