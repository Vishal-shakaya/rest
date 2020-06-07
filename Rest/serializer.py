from rest_framework import serializers
from Rest import models
class Serializer_view(serializers.Serializer):
    """ returning name """
    name = serializers.CharField(max_length=255)



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MyUser
        fields = ['id','email','name','password']

        extra_kwargs = {
        'password': {
        'write_only': True,
        'style':{'input_type':'password'}

          }
        }

    def create(self ,validated_data):
    	user = models.MyUser.objects.create_user(
    		email=validated_data['email'],
    		name=validated_data['name'],
    		password=validated_data['password'])

    	return user

    
