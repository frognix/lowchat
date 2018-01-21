# Generated by Django 2.0 on 2018-01-16 16:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('chat', '0002_auto_20180109_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='Features',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('information', models.CharField(max_length=1024)),
                ('namecolor', models.CharField(default='black', max_length=32)),
            ],
        ),
    ]
