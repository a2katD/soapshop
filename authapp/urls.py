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
from django.urls import path

from authapp.views import login, register, profile, logout

app_name = 'authapp'

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('logout/', logout, name='logout'),
]
