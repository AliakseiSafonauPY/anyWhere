# Generated by Django 5.0 on 2024-01-04 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('copyright_contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='contact_icon',
            field=models.ImageField(blank=True, null=True, upload_to='./img/icons', verbose_name='Иконка'),
        ),
    ]