# Generated by Django 4.1.6 on 2023-04-29 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_remove_customuser_district_id_no_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='district_id_no',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='state_id_no',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
