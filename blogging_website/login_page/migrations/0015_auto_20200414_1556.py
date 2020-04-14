# Generated by Django 2.2.4 on 2020-04-14 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_page', '0014_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactform',
            name='body',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='contactform',
            name='email',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='contactform',
            name='subject',
            field=models.CharField(default=None, max_length=100),
        ),
    ]