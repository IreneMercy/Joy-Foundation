# Generated by Django 3.0 on 2020-03-21 16:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('joy', '0003_gallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='events',
            options={'ordering': ['pub_date']},
        ),
        migrations.AlterModelOptions(
            name='gallery',
            options={'ordering': ['pub_date']},
        ),
        migrations.AddField(
            model_name='gallery',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='events',
            name='venue',
            field=models.CharField(max_length=100),
        ),
    ]