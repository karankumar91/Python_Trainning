from rest_framework import serializers
from .models import student

class StudenSerilizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=student
        fields="__all__"