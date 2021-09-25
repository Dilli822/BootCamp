
# Serailizer convert the complex data types into python native data types
# it deserailize the json format data into python data native type
from rest_framework import serializers

#importing modeles for more shortcut method
from .models import Info

class AddTwoNumberSerializer(serializers.Serializer):
    number1 = serializers.IntegerField()
    number2 = serializers.IntegerField()



class InfoSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    address= serializers.CharField(max_length=100)


    # more shortcut method for update and create method
    def create(self, validated_data):
        print("context on serializer---->", self.context)
        return Info.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.address = validated_data['address']
        instance.save()
        return instance


class InfoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Info
        fields = ['name', 'address']


# we created class basedView with status code and used serializer
