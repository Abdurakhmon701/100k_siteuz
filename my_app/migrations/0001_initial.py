# Generated by Django 4.1.2 on 2022-10-18 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zagolovok', models.CharField(max_length=200)),
                ('opisaniye', models.TextField()),
                ('tsena', models.CharField(max_length=20)),
                ('foto', models.ImageField(upload_to='images/')),
            ],
        ),
    ]