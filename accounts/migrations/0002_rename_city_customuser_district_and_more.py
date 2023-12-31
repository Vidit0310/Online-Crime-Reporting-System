# Generated by Django 4.1.6 on 2023-04-29 09:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='city',
            new_name='district',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='country',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='is_active',
        ),
        migrations.AddField(
            model_name='customuser',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='is_user',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
