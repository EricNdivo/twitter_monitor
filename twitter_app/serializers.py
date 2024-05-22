from rest_framework import serializers

class TweetSerializer(serializers.Serializer):
    message = serializers.CharField(max_length=20)

class KeywordSerializer(serializers.Serializer):
    keyword = serializers.CharField(max_length=100)
    count = serializers.IntegerField(default=10)
    