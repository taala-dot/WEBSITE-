# Generated by Django 5.1.1 on 2024-10-23 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='first_slide_text',
            field=models.CharField(default='Saúde natural para os seus cabelos', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='second_slide_text',
            field=models.CharField(default='Sobre nós', max_length=255),
        ),
        migrations.AddField(
            model_name='homepage',
            name='third_slide_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='homepage',
            name='third_slide_text',
            field=models.CharField(default='Seu texto для третьего слайда', max_length=255),
        ),
    ]