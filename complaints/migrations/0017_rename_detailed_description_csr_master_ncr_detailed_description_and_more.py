# Generated by Django 4.1.6 on 2023-05-01 10:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0016_csr_master'),
    ]

    operations = [
        migrations.RenameField(
            model_name='csr_master',
            old_name='detailed_description',
            new_name='ncr_detailed_description',
        ),
        migrations.AlterField(
            model_name='csr_master',
            name='created_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='csr_master',
            name='updated_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
