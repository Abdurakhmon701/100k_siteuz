from django.urls import path,include
from .views import *
from rest_framework.routers import DefaultRouter


# router = DefaultRouter()

# router.register('mahsulotlar',HomePageAPIView)

urlpatterns = [
	path('mahsulotlar/',HomePageAPIView.as_view()),
	path('category/',CategoryAPIView.as_view()),
	path('mahsulotlarr/<int:pk>/',ProductById.as_view()),
	]