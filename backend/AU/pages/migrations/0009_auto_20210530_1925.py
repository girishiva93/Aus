# Generated by Django 3.1.7 on 2021-05-30 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0008_auto_20210530_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroslider',
            name='slider_image_button_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='heroslider',
            name='slider_image_description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='heroslider',
            name='slider_image_title',
            field=models.CharField(max_length=100),
        ),
    ]
