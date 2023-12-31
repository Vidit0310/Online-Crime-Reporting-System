# Generated by Django 4.1.6 on 2023-04-30 18:03

import accounts.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('complaints', '0015_alter_complaint_master_status_id_and_more'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('accounts', '0018_alter_customuser_aadhaarno_alter_customuser_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='rank_master',
            fields=[
                ('rank_id', models.AutoField(primary_key=True, serialize=False)),
                ('rank_name', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='customuser_groups', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, related_name='customuser_permissions', to='auth.permission'),
        ),
        migrations.CreateModel(
            name='police_incharge',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('incharge_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('Phone_Number', models.IntegerField()),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=128)),
                ('gender', models.CharField(max_length=7)),
                ('aadhaarno', models.IntegerField()),
                ('rank_id', models.IntegerField(blank=True, null=True)),
                ('profile_image', models.ImageField(blank=True, default='media/Profile\\ images/default.png', null=True, upload_to='Profile images/')),
                ('address', models.CharField(max_length=500)),
                ('pincode', models.IntegerField()),
                ('state_id_no', models.IntegerField(blank=True, null=True)),
                ('district_id_no', models.IntegerField(blank=True, null=True)),
                ('status_id', models.CharField(choices=[('active', 'active'), ('inactive', 'inactive'), ('deleted', 'deleted'), ('suspended', 'suspended')], max_length=10)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='complaint_in_district+', to='complaints.district_master', to_field='district_name')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='police_incharge_groups', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('rank_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='accounts.rank_master', to_field='rank_name')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='state+', to='complaints.state_master', to_field='state_name')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='policeincharge_permissions', to='auth.permission')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', accounts.models.CustomUserManager()),
            ],
        ),
    ]
