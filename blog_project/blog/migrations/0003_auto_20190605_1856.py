# Generated by Django 2.2.1 on 2019-06-05 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_noticeboard'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticeboard',
            old_name='body_notice',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='noticeboard',
            old_name='title_notice',
            new_name='title',
        ),
    ]
