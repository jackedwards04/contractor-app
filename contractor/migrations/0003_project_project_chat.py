# Generated by Django 3.0.2 on 2020-05-07 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractor', '0002_auto_20200507_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_chat',
            field=models.TextField(default='testing'),
            preserve_default=False,
        ),
    ]
