from rest_framework import serializers
from .models import Logdb

class Logserializer(serializers.ModelSerializer):

    class Meta:
        model = Logdb
        fields = ["verb", "path", "status", "duration", "payload", "header", "responses", "happened"]