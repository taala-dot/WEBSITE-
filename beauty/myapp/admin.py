from django.contrib import admin
from .models import HomePage,AboutUs,Testimonials
class TestimonialsAdmin(admin.ModelAdmin):
    list_display = ('girl_one_name', 'girl_two_name')
    search_fields = ('girl_one_name', 'girl_two_name')

admin.site.register(Testimonials, TestimonialsAdmin)


class HomePageAdmin(admin.ModelAdmin):
    list_display = ('first_slide_title',)
    search_fields = ('first_slide_title',)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('title',)

admin.site.register(HomePage, HomePageAdmin)
admin.site.register(AboutUs, AboutUsAdmin)

