# Generated by Django 2.2.10 on 2020-04-20 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('joy', '0029_auto_20200420_1119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=155),
        ),
    ]
