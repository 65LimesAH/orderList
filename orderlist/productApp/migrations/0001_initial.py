# Generated by Django 3.1.4 on 2021-01-04 23:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='DEFAULT VALUE', max_length=55, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='DEFAULT VALUE', max_length=55, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='DEFAULT VALUE', max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('alternateName', models.CharField(max_length=55)),
                ('price', models.IntegerField(default=0)),
                ('attributes', models.ManyToManyField(to='productApp.Attributes')),
                ('categories', models.ManyToManyField(to='productApp.Categories')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='productApp.unit')),
            ],
        ),
    ]