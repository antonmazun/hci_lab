# Generated by Django 2.1.3 on 2018-11-05 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0009_auto_20181105_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Backet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Laptop')),
            ],
        ),
    ]
