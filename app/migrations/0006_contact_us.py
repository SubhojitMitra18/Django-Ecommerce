# Generated by Django 3.2.20 on 2023-11-01 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_order'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_us',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
