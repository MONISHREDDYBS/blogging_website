# Generated by Django 2.2.4 on 2020-04-10 08:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_page', '0005_auto_20200410_1409'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='name',
            new_name='username1',
        ),
    ]