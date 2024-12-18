# Generated by Django 5.1.3 on 2024-12-11 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClinicalData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('componentName', models.CharField(choices=[('hw', 'Height/Weight'), ('bp', 'Blood Pressure'), ('heartrate', 'Heart Rate')], max_length=20)),
                ('componentValue', models.CharField(max_length=20)),
                ('measuredDateTime', models.DateTimeField(auto_now_add=True)),
                ('patient_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastName', models.CharField(max_length=20)),
                ('firstName', models.CharField(max_length=20)),
                ('dob', models.DateField(max_length=8)),
            ],
        ),
    ]
