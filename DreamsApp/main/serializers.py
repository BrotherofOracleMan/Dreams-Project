from rest_framework import serializers
from main.models import Dream

class DreamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dream
        fields = ['id','date','quote']
