# Generated by Django 5.1.1 on 2024-09-25 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_student_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='Image',
            field=models.ImageField(max_length=255, upload_to='img/'),
        ),
    ]
