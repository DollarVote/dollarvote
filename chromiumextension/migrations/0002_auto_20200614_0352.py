# Generated by Django 3.0.5 on 2020-06-14 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chromiumextension', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='impact',
            old_name='score',
            new_name='blm',
        ),
        migrations.AddField(
            model_name='impact',
            name='climate',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='impact',
            name='healthcare',
            field=models.FloatField(default=0.0),
            preserve_default=False,
        ),
    ]
