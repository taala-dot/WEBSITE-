# Generated by Django 5.1.1 on 2024-10-23 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_slide_image', models.ImageField(upload_to='images/')),
                ('second_slide_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]