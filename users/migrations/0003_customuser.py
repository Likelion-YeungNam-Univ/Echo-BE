# Generated by Django 3.2.2 on 2023-08-11 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.BigAutoField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('username', models.CharField(max_length=45)),
                ('nickname', models.CharField(max_length=45, unique=True)),
                ('bio', models.TextField(max_length=256)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'db_table': 'users',
            },
        ),
    ]
