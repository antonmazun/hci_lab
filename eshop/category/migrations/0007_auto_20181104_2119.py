# Generated by Django 2.1.3 on 2018-11-04 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_auto_20181104_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='laptop',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/', verbose_name='Картинка'),
        ),
    ]