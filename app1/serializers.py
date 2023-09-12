from rest_framework import serializers
from .models import SiyosiyNewModel,IjtimoiyNewModels


class siyo_serializer(serializers.ModelSerializer):
    class Meta:
        model = SiyosiyNewModel
        fields = ('new_text','pub_data')

class ijti_serializer(serializers.ModelSerializer):
    class Meta:
        model = IjtimoiyNewModels
        fields = ('new_text','pub_data')