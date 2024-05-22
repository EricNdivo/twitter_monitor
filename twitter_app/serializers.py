from rest_framework import serializers

class TweetSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=20)

class KeywordSerializer(serializers.Serializer):
    keyword = serializers.CharField(max_length=100)
    count = serializers.IntegerField(default=10)

class TweetSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=280)

class KeywordSerializer(serializers.Serializer):
    keyword = serializers.CharField(max_length=100)
    count = serializers.IntegerField()

class UsernameSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
