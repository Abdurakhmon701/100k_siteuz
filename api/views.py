from django.shortcuts import render
from .serializers import HomePageSerializers
from rest_framework.viewsets import ModelViewSet
from my_app.models import HomePageModel


class HomePageAPIView(ModelViewSet):
	queryset = HomePageModel.objects.all()
	serializer_class = HomePageSerializers
