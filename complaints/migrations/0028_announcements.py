# Generated by Django 4.1.6 on 2023-06-24 12:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0027_csr_master_feedback_fir_master_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='announcements',
            fields=[
                ('announcements_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=5000)),
                ('image', models.ImageField(blank=True, null=True, upload_to='announcements images/')),
                ('created_at', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'announcements',
            },
        ),
    ]
