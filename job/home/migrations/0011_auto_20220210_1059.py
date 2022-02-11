# Generated by Django 3.2.9 on 2022-02-10 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_rename_title_application_job_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(null=True, upload_to='logoimages'),
        ),
        migrations.AlterField(
            model_name='application',
            name='job_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.job'),
        ),
    ]
