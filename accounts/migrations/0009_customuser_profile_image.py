# Generated by Django 4.1.6 on 2023-04-29 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_customuser_district_id_no_customuser_state_id_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='profile_image',
            field=models.ImageField(blank=True, default='Profile images/default', null=True, upload_to='Profile images/'),
        ),
    ]
