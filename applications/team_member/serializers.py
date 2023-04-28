from rest_framework import serializers
from .models import Member


class MemberListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


class MemberDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'
