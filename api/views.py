from django.shortcuts import render
from .serializers import *
# from rest_framework.viewsets import ModelViewSet,
from my_app.models import *
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response


# class HomePageAPIView(ModelViewSet):
# 	queryset = HomePageModel.objects.all()
# 	serializer_class = HomePageSerializers

class HomePageAPIView(ListAPIView):
	queryset = HomePageModel.objects.all()
	serializer_class  = HomePageSerializers

class CategoryAPIView(ListAPIView):
	queryset = Category.objects.all()
	serializer_class  = CategorySerializers

class ProductById(APIView):
	def get_object(self, pk):
		try:
			cat = Category.objects.get(pk=pk)
			return HomePageModel.objects.all().filter(category=pk)
			print(HomePageModel.objects.filter(category=pk))
		except HomePageModel.DoesNotExist:
			raise Http404
	def get(self, request, pk):
		snippet = self.get_object(pk)
		serializer = HomePageSerializers(snippet)
		response = {
		'message':'salom'}
		return Response(serializer.data)

# class ProductById(APIView):

# 	def get(self, request, pk):
# 		serializer_class = HomePageSerializers
# 		user = HomePageModel.objects.filter(category_id=pk)
# 		response = {
# 		'message':'salom'}
# 		return Response(user)