
from rest_framework import serializers

class AddTwoNumbersSerializer(serializers.Serializer):
    number1 = serializers.IntegerField()
    number2 = serializers.IntegerField()

