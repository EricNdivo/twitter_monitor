# twitter_app/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TweetSerializer, KeywordSerializer
from .twitter_service import TwitterService
from django.conf import settings

twitter_service = TwitterService(
    api_key=settings.TWITTER_API_KEY,
    api_secret_key=settings.TWITTER_API_SECRET_KEY,
    access_token=settings.TWITTER_ACCESS_TOKEN,
    access_token_secret=settings.TWITTER_ACCESS_TOKEN_SECRET
)

class TweetView(APIView):
    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        if serializer.is_valid():
            twitter_service.tweet(serializer.validated_data['message'])
            return Response({'status': 'Tweet sent'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MonitorTweetsView(APIView):
    def post(self, request):
        serializer = KeywordSerializer(data=request.data)
        if serializer.is_valid():
            tweets = twitter_service.get_tweets(
                keyword=serializer.validated_data['keyword'],
                count=serializer.validated_data['count']
            )
            return Response(tweets, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
