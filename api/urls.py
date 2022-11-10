from django.urls import path,include
from .views import HomePageAPIView
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('mahsulotlar',HomePageAPIView)

urlpatterns = [
	path('',include(router.urls))
	]