
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

    message = serializers.SerializerMethodField()
        
    class Meta:
        model = Info
        fields = ['id', 'name', 'address','message']
        # for not allowing to post method
        read_only_fields = ['id']

    @staticmethod
    def get_message(obj):
        name = obj.name
        return f"Hi, I am {name}"
    
    

    # we created class basedView with status code and used 
    # validaiton 
    # 1. name length validation
    @staticmethod
    def validate_name(name):
        if len(name) <=  1:
            raise serializers.ValidationError("length of name should be greater than 1")
        return name

    # normal name and address validation
    def validate(self, data):
        name =data['name']
        address = data['address']
        if name == address:
            raise serializers.ValidationError("Name and Address cannot be same!")
        return data
    
