# Generated by Django 3.1.4 on 2021-01-04 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('productApp', '0001_initial'),
        ('organizationsApp', '0001_initial'),
        ('orderListApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlist',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organizationsApp.organization'),
        ),
        migrations.AddField(
            model_name='orderlist',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productApp.products'),
        ),
    ]
