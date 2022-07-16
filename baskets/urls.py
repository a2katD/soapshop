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
from baskets.views import basket_add, basket_remove

app_name = 'baskets'

urlpatterns = [
    path('add/<int:id>', basket_add, name='basket_add'),
    path('remove/<int:basket_id>', basket_remove, name='basket_remove'),
]
