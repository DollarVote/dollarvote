# Generated by Django 3.0.5 on 2020-07-06 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chromiumextension', '0007_company_parent_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='opensecrets_id',
            field=models.CharField(max_length=16, null=True),
        ),
    ]