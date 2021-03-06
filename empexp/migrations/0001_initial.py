# Generated by Django 3.1.12 on 2021-06-27 05:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('site02', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('companyname', models.CharField(max_length=200)),
                ('fromdate', models.DateField()),
                ('todate', models.DateField()),
                ('rolesandresponsibility', models.TextField()),
                ('reasonofleaving', models.TextField()),
                ('currentexperience', models.BooleanField(default=True)),
                ('employee', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='site02.employee')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
