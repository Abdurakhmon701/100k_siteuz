from rest_framework import serializers
from my_app.models import HomePageModel,Category

class HomePageSerializers(serializers.ModelSerializer):
	class Meta:
		model = HomePageModel
		fields = '__all__'
		# fields = ('id',)

class CategorySerializers(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'