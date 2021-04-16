# Generated by Django 3.1.7 on 2021-04-16 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('academic', '0002_paper_authors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paper',
            name='link',
            field=models.URLField(null=True, verbose_name='Link'),
        ),
        migrations.AlterField(
            model_name='talk',
            name='abstract',
            field=models.TextField(blank=True, verbose_name='Abstract'),
        ),
    ]
