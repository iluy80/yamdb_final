# Generated by Django 2.2.16 on 2022-05-13 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20220512_2312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(blank=True, max_length=256, verbose_name='Код подтверждения'),
        ),
    ]
