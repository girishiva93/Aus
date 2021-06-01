# Generated by Django 3.1.1 on 2021-06-01 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_title', models.CharField(max_length=400)),
                ('image', models.ImageField(upload_to='photos/%Y/%m/%d/')),
            ],
        ),
    ]