# Generated by Django 3.2 on 2021-06-06 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0012_auto_20210605_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='id_card_number',
            field=models.CharField(default='4648684864', max_length=25),
            preserve_default=False,
        ),
    ]
