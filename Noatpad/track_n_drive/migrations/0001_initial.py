# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-30 22:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('make', models.CharField(default='make', help_text='Enter the make of the car.', max_length=50)),
                ('model', models.CharField(default='model', help_text='Enter the model of the car.', max_length=50)),
                ('year', models.IntegerField(default=1, help_text='Enter the year of the car.', max_length=10)),
                ('engine_type', models.CharField(help_text='Enter the engine type of the car.', max_length=50, null=True)),
                ('mileage', models.IntegerField(help_text='Enter the mileage of the car', max_length=15, null=True)),
                ('oil_type', models.CharField(help_text='Enter the oil type of the car.', max_length=50, null=True)),
                ('color', models.CharField(default='color', help_text='Enter the color of the car.', max_length=50)),
                ('registration', models.CharField(help_text='Enter the registration of the car.', max_length=50, null=True)),
                ('vin_number', models.CharField(help_text='Enter the vin number of the car', max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('address', models.EmailField(default='you@example.com', help_text='Enter your Email.', max_length=254, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='EmailTimings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.IntegerField(default=1, help_text='How many times should you be reminded?')),
                ('reminder', models.CharField(blank=True, choices=[('w', 'Weeks Before'), ('d', 'Days Before')], default='w', help_text='Alert Type', max_length=1)),
                ('email', models.ForeignKey(help_text='Select an email.', on_delete=django.db.models.deletion.CASCADE, to='track_n_drive.Email')),
            ],
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('insurance_num', models.CharField(default='Ins. #', help_text='Enter your insurance number', max_length=30, primary_key=True, serialize=False)),
                ('company', models.CharField(help_text='Enter your company', max_length=30, null=True)),
                ('coverage', models.CharField(help_text='Enter your coverage', max_length=30, null=True)),
                ('expiration_date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='License',
            fields=[
                ('license_num', models.CharField(help_text='Enter your license number', max_length=50, primary_key=True, serialize=False)),
                ('license_class', models.CharField(help_text='Enter your license class', max_length=50)),
                ('expiration_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Notifications',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('date', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('number', models.CharField(default='0000000000', help_text='Enter your phone number.', max_length=15, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneTimings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frequency', models.IntegerField(default=1, help_text='How many times should you be reminded?')),
                ('reminder', models.CharField(blank=True, choices=[('w', 'Weeks Before'), ('d', 'Days Before')], default='w', help_text='Alert Type', max_length=1)),
                ('phone', models.ForeignKey(help_text='Select a Phone.', on_delete=django.db.models.deletion.CASCADE, to='track_n_drive.Phone')),
            ],
        ),
        migrations.CreateModel(
            name='Repair',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter the name for the repair.', max_length=200)),
                ('cost', models.CharField(help_text='Enter them cost for the repair', max_length=20)),
                ('date_made', models.DateField(default=datetime.date(2017, 10, 30))),
                ('car', models.ForeignKey(help_text='Select the car that was repaired', on_delete=django.db.models.deletion.CASCADE, to='track_n_drive.Car')),
            ],
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.ForeignKey(help_text='Select an email', on_delete=django.db.models.deletion.CASCADE, to='track_n_drive.Email')),
                ('phone', models.ForeignKey(help_text='Select a phone', on_delete=django.db.models.deletion.CASCADE, to='track_n_drive.Phone')),
            ],
        ),
        migrations.CreateModel(
            name='TechAddedInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information_name', models.CharField(default='info name', help_text='Information Category', max_length=200)),
                ('information_contents', models.CharField(default='info content', help_text='Information to Add', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Technician',
            fields=[
                ('unique_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fname', models.CharField(help_text='Enter technician first name.', max_length=30)),
                ('lname', models.CharField(help_text='Enter technician last name.', max_length=30)),
                ('street', models.CharField(help_text='Enter the street address of the technician.', max_length=100)),
                ('city', models.CharField(help_text='Enter the city of the technician.', max_length=100)),
                ('company', models.CharField(blank=True, help_text='Enter the company of the technician.', max_length=100, null=True)),
                ('other_info', models.ManyToManyField(blank=True, help_text='Additional Information', null=True, to='track_n_drive.TechAddedInfo')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('fname', models.CharField(help_text='Enter your first name.', max_length=30)),
                ('lname', models.CharField(help_text='Enter your last name.', max_length=30)),
                ('password', models.CharField(help_text='Enter your password.', max_length=30)),
                ('cars', models.ManyToManyField(default=True, help_text='Select a car for this User.', null=True, to='track_n_drive.Car')),
                ('insurance', models.ForeignKey(blank=True, help_text='Select a insurance for this User.', null=True, on_delete=django.db.models.deletion.CASCADE, to='track_n_drive.Insurance')),
                ('license', models.ForeignKey(blank=True, help_text='Select a license for this User.', null=True, on_delete=django.db.models.deletion.CASCADE, to='track_n_drive.License')),
                ('notifications', models.ForeignKey(blank=True, help_text='Notifications for this User.', null=True, on_delete=django.db.models.deletion.CASCADE, to='track_n_drive.Notifications')),
            ],
        ),
        migrations.CreateModel(
            name='UserAddedInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('information_name', models.CharField(default='info name', help_text='Information Category', max_length=200)),
                ('information_contents', models.CharField(default='info content', help_text='Information to Add', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='other_info',
            field=models.ForeignKey(blank=True, help_text='Enter user info.', null=True, on_delete=django.db.models.deletion.CASCADE, to='track_n_drive.UserAddedInfo'),
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.ForeignKey(blank=True, help_text='Select a phone for this User.', null=True, on_delete=django.db.models.deletion.CASCADE, to='track_n_drive.Phone'),
        ),
        migrations.AddField(
            model_name='user',
            name='settings',
            field=models.ForeignKey(help_text='Select settings', on_delete=django.db.models.deletion.CASCADE, to='track_n_drive.Settings'),
        ),
        migrations.AddField(
            model_name='user',
            name='technician',
            field=models.ManyToManyField(blank=True, help_text='Select a Technician for this User.', null=True, to='track_n_drive.Technician'),
        ),
        migrations.AddField(
            model_name='repair',
            name='technician',
            field=models.ForeignKey(blank=True, help_text='Select the technician for the repair', null=True, on_delete=django.db.models.deletion.CASCADE, to='track_n_drive.Technician'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='email_timings',
            field=models.ManyToManyField(help_text='When should you be notified via email?', to='track_n_drive.PhoneTimings'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='phone_timings',
            field=models.ManyToManyField(help_text='When should you be notified via phone?', to='track_n_drive.EmailTimings'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='repair',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='track_n_drive.Repair'),
        ),
        migrations.AddField(
            model_name='notifications',
            name='technician',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='track_n_drive.Technician'),
        ),
    ]
