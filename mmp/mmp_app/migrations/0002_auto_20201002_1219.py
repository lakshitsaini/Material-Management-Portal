# Generated by Django 3.1.2 on 2020-10-02 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmp_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='files',
            field=models.FileField(blank=True, null=True, upload_to='Files/'),
        ),
        migrations.DeleteModel(
            name='UploadFile',
        ),
    ]
