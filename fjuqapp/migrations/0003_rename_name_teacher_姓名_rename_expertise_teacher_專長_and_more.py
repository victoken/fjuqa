# Generated by Django 4.2.3 on 2023-07-21 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fjuqapp', '0002_teacher_delete_user_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teacher',
            old_name='name',
            new_name='姓名',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='expertise',
            new_name='專長',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='contact_number',
            new_name='聯絡方式',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='office_location',
            new_name='辦公室位置',
        ),
    ]
