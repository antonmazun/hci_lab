# Generated by Django 2.1.3 on 2018-11-04 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_laptop_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='Картинка'),
        ),
    ]
