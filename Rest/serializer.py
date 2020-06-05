from rest_framework import serializers

class Serializer_view(serializers.Serializer):
    """ returning name """
    name = serializers.CharField(max_length=255)
