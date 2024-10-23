from django.db import models


class HomePage(models.Model):
    first_slide_title = models.CharField(max_length=200, blank=True, null=True)
    first_slide_text = models.TextField(blank=True, null=True)
    first_slide_image = models.ImageField(upload_to='slides/', blank=True, null=True)

    def __str__(self):
        return self.first_slide_title if self.first_slide_title else "Home Page"


class AboutUs(models.Model):
    image = models.ImageField(upload_to='about/', verbose_name='Изображение')
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title
class Testimonials(models.Model):
    girl_one_name = models.CharField(max_length=255)
    girl_one_testimonial = models.TextField()
    girl_two_name = models.CharField(max_length=255)
    girl_two_testimonial = models.TextField()
    image_one = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    image_two = models.ImageField(upload_to='testimonials/', blank=True, null=True)

    def __str__(self):
        return f"{self.girl_one_name} and {self.girl_two_name} Testimonials"
