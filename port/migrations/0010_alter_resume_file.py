# Generated by Django 4.2 on 2024-03-10 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('port', '0009_alter_resume_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='file',
            field=models.FileField(upload_to='files'),
        ),
    ]