# Generated by Django 4.1 on 2022-08-31 12:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('alias', models.CharField(max_length=20, unique=True)),
                ('password', models.BinaryField(max_length=60)),
                ('salt', models.BinaryField(max_length=29)),
                ('email', models.CharField(max_length=50)),
                ('active', models.BooleanField(default=True)),
                ('autosave', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
