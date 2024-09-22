from rest_framework import serializers
from .models import B



class BSerializer(serializers.ModelSerializer):
    class Meta:
        model = B
        fields = ['a', 'dic_value']


# from rest_framework import serializers
# from .models import B

# class BSerializer(serializers.ModelSerializer):
#     a = serializers.StringRelatedField(source='a.name')

#     class Meta:
#         model = B
#         fields = ['id', 'a', 'dic_value', 'created_at', 'updated_at']

#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data['a'] = instance.a.name
#         return data