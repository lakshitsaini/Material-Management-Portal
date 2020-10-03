# Generated by Django 3.1.2 on 2020-10-03 04:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mmp_app', '0004_auto_20201003_0947'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='id',
            field=models.AutoField(auto_created=True, default='', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='faculty',
            name='id',
            field=models.AutoField(auto_created=True, default='', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='id',
            field=models.AutoField(auto_created=True, default='', primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='course',
            name='course_name',
            field=models.CharField(max_length=256),
        ),
        migrations.RemoveField(
            model_name='faculty',
            name='courses',
        ),
        migrations.AddField(
            model_name='faculty',
            name='courses',
            field=models.ManyToManyField(to='mmp_app.Course'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='student',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
