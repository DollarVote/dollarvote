# Generated by Django 3.0.5 on 2020-07-08 21:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chromiumextension', '0009_auto_20200708_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='id',
        ),
        migrations.AlterField(
            model_name='company',
            name='opensecrets_id',
            field=models.CharField(max_length=16, primary_key=True, serialize=False),
        ),
    ]