# Generated by Django 3.2.19 on 2024-02-08 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='bio',
            field=models.TextField(default='none', max_length=1024),
            preserve_default=False,
        ),
    ]
