from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from myapp import views as user_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('lk/', user_views.lk_view, name='lk'),  # Личный кабинет
    path('', user_views.index, name='index'),  # Главная страница
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Страница входа
    path('register/', user_views.register, name='register'),  # Страница регистрации
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
