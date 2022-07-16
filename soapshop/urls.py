"""soapshop URL Configuration
Здесь хранятся пути к контроллерам,
то есть когда мы переходим на определенный урл,
он вызывает контроллер выполняющий определенные действия
https://docs.djangoproject.com/en/4.0/topics/http/urls/
Примеры:
Представления функций
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Представления на основе классов
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Включение другой конфигурации URL
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from mainapp.views import index, products

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', include('mainapp.urls', namespace='mainapp')),
    path('users/', include('authapp.urls', namespace='authapp')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
