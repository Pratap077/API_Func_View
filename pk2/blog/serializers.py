from rest_framework import serializers

class BlockData(serializers.Serializer):
  id=serializers.IntegerField()
  name=serializers.CharField(max_length=50)
  email=serializers.EmailField(max_length=50)
  mobile=serializers.IntegerField()
  city=serializers.CharField(max_length=50)
 

