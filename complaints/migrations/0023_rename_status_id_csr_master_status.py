# Generated by Django 4.1.6 on 2023-05-03 13:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0022_rename_status_id_fir_master_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='csr_master',
            old_name='status_id',
            new_name='status',
        ),
    ]
