# Generated by Django 4.2.5 on 2023-11-21 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocrNumber', models.CharField(max_length=13)),
                ('bgNumber', models.CharField(max_length=20)),
                ('price', models.FloatField()),
                ('refNumber', models.CharField(max_length=20)),
                ('isPaid', models.BooleanField()),
                ('refrence', models.CharField(max_length=20)),
                ('dueDate', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='UploadedFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='uploads/')),
            ],
        ),
    ]
