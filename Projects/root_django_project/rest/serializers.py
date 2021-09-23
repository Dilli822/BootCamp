
# Serailizer convert the complex data types into python native data types
# it deserailize the json format data into python data native type
from rest_framework import serializers

class AddTwoNumberSerializer(serializers.Serializer):
    number1 = serializers.IntegerField()
    number2 = serializers.IntegerField()



class InfoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    address= serializers.CharField(max_length=100)


