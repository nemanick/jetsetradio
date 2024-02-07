# Generated by Django 3.2.9 on 2022-03-10 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=220)),
                ('description', models.TextField(blank=True, null=True)),
                ('album_image', models.ImageField(default='AlbumsImages/default.jpg', upload_to='AlbumsImages/')),
                ('album_download_link_high', models.CharField(blank=True, max_length=350, null=True)),
                ('album_download_link_medium', models.CharField(blank=True, max_length=350, null=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('release_time', models.DateField(blank=True, null=True)),
                ('published', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
