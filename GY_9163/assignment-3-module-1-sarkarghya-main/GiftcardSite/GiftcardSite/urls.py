"""GiftcardSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.views import static
from django.conf import settings

urlpatterns = [
    path('images/<str:path>/', static.serve, {'document_root': settings.IMAGE_ROOT}),
    path('js/<str:path>/', static.serve, {'document_root': settings.JS_ROOT}),
    path('css/<str:path>/', static.serve, {'document_root': settings.CSS_ROOT}),
    path('fonts/<str:path>/', static.serve, {'document_root': settings.FONT_ROOT}),
    path('', include('LegacySite.urls')),
    path('admin/', admin.site.urls),
]
