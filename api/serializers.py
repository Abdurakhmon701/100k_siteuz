from rest_framework import serializers
from my_app.models import HomePageModel

class HomePageSerializers(serializers.ModelSerializer):
	class Meta:
		model = HomePageModel
		fields = '__all__'
		# fields = ('id','zagolovok')