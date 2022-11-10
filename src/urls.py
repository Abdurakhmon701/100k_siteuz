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
from django.urls import path,include
from my_app import views

from django.conf import settings
from django.conf.urls.static import static

from users import views as user


urlpatterns = [
    path('admin/', admin.site.urls),

    #api uchun url
    path('api/v1',include('api.urls')),




    #templates uchun urllar
    path('',views.homePageView,name='main'),
    path('aloqa/',views.AloqaPageView.as_view(),name = 'aloqa'),

    path('login/',user.loginPage,name = 'login'),

    path('sevimlilar/',views.SevimliPageView.as_view(),name = 'sevimlilarim'),

    path('plyus/',views.PlyusPageView.as_view(),name='plyus'),
    path('buyurtma/',views.BuyurtmaPageView.as_view(),name='buyurtma'),
    path('bildirishnoma/',views.BildirishnomaPageView.as_view(),name='bildirishnoma'),
    path('sozlamalar/<str:user_id>/',user.profil_settings),

    path('profil/',views.ProfilPageView.as_view(),name = 'prf'),
    path('oferta/',views.OffertaPageView.as_view(),name = "offerta"),
    path('barchasi/',views.BarchasiPageView.as_view(),name = 'barchasi'),
    path('detail/<int:pk>',views.DetailPageView.as_view(),name = 'detail'),
    path('category/<str:category_id>/',views.categoryPageView,name='category'),


    path('signup/',user.signUpView,name='signup'),
    path('logout/',user.logout_user,name='logout'),
    

]+static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)
