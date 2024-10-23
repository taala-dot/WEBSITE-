# Generated by Django 5.1.1 on 2024-10-23 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_aboutus_delete_aboutsection_delete_contactinfo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('girl_one_name', models.CharField(max_length=255)),
                ('girl_one_testimonial', models.TextField()),
                ('girl_two_name', models.CharField(max_length=255)),
                ('girl_two_testimonial', models.TextField()),
                ('image_one', models.ImageField(blank=True, null=True, upload_to='testimonials/')),
                ('image_two', models.ImageField(blank=True, null=True, upload_to='testimonials/')),
            ],
        ),
    ]
