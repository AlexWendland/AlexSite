# Generated by Django 3.1.7 on 2021-04-16 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='authors',
            field=models.TextField(default=None, verbose_name='Authors'),
            preserve_default=False,
        ),
    ]
