# Generated by Django 5.2.3 on 2025-07-02 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_student_registration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='registration_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
