# Generated by Django 3.1.8 on 2022-06-19 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('money_management', '0003_auto_20220618_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
