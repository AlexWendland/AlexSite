# Generated by Django 3.1.7 on 2021-04-19 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0003_auto_20210416_1541'),
    ]

    operations = [
        migrations.AddField(
            model_name='talk',
            name='seminar_name',
            field=models.CharField(default='a', max_length=200, verbose_name='Location'),
            preserve_default=False,
        ),
    ]
