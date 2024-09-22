from rest_framework import serializers
from .models import A


class ASerializer(serializers.ModelSerializer):
    class Meta:
        model = A
        fields = ["name", "value", "created_at", "updated_at"]
