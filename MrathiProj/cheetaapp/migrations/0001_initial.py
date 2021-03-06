# Generated by Django 2.2.3 on 2020-06-08 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=120, null=True)),
                ('location', models.CharField(blank=True, max_length=120, null=True)),
                ('experience', models.CharField(blank=True, max_length=120, null=True)),
                ('qualification', models.CharField(blank=True, max_length=120, null=True)),
                ('salary', models.CharField(blank=True, max_length=120, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='cards')),
            ],
        ),
    ]
