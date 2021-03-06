# Generated by Django 3.2.9 on 2022-02-07 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=120)),
                ('last_name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=120)),
                ('phone', models.PositiveIntegerField(max_length=12)),
                ('location', models.CharField(max_length=120)),
                ('experience', models.PositiveIntegerField(max_length=5)),
                ('qualification', models.CharField(max_length=120)),
                ('skills', models.CharField(max_length=300)),
                ('income', models.PositiveIntegerField(max_length=120)),
            ],
        ),
    ]
