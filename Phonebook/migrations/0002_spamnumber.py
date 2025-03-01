# Generated by Django 4.2.18 on 2025-01-15 20:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Phonebook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpamNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15, unique=True)),
                ('reported_at', models.DateTimeField(auto_now_add=True)),
                ('reported_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
