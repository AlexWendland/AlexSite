# Generated by Django 3.1.7 on 2021-04-19 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0004_talk_seminar_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='seminar_name',
            field=models.CharField(max_length=200, verbose_name='Seminar Name'),
        ),
    ]