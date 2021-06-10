# Generated by Django 3.2 on 2021-06-06 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0013_student_id_card_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='age_level',
            new_name='gender',
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
