# Generated by Django 4.1.6 on 2023-05-01 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0022_police_incharge_is_active_police_incharge_is_staff_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='police_incharge',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='police_incharge_groups', related_query_name='police_incharge', to='auth.group', verbose_name='groups'),
        ),
    ]
