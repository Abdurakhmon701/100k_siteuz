"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from my_app import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homePageView),
    path('aloqa/',views.AloqaPageView.as_view(),name = 'aloqa'),
    path('login/',views.LoginPageView.as_view(),name = 'login'),
    path('sevimlilar/',views.SevimliPageView.as_view(),name = 'sevimlilarim'),
    path('sozlamalar/',views.SozlamalarPageView.as_view(),name = 'sozlamalar'),
    path('profil/',views.ProfilPageView.as_view(),name = 'prf'),
    path('oferta/',views.OffertaPageView.as_view(),name = "offerta"),
    path('barchasi/',views.BarchasiPageView.as_view(),name = 'barchasi'),
    path('detail/<int:pk>',views.DetailPageView.as_view(),name = 'detail'),
    path('category/<str:category_id>/',views.categoryPageView,name='category'),
]+static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
