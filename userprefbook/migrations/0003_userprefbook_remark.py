# Generated by Django 3.1.12 on 2021-06-29 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprefbook', '0002_remove_userprefbook_remark'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprefbook',
            name='remark',
            field=models.TextField(null=True),
        ),
    ]
