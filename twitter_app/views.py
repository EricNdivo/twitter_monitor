from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import TweetSerializer, KeywordSerializer, UsernameSerializer
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
            # Handle the tweet logic
            return Response({'message': 'Tweet posted successfully!'}, status=status.HTTP_200_OK)
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


class UserInfoView(APIView):
    def post(self, request):
        serializer = UsernameSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            
            # Access Twitter API credentials from settings
            api_key = settings.TWITTER_API_KEY
            api_secret_key = settings.TWITTER_API_SECRET_KEY
            access_token = settings.TWITTER_ACCESS_TOKEN
            access_token_secret = settings.TWITTER_ACCESS_TOKEN_SECRET
            
            twitter_service = TwitterService(api_key, api_secret_key, access_token, access_token_secret)
            user_data = twitter_service.get_user_info(username)
            if user_data:
                return Response(user_data, status=status.HTTP_200_OK)
            else:
                error_message = 'User not found or other error occurred.'
                return Response({'error': error_message}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
class ReplyTweetView(APIView):
    def post(self, request):
        serializer = TweetSerializer(data=request.data)
        tweet_id = request.data.get('tweet_id')
        if serializer.is_valid() and tweet_id:
            twitter_service.reply_to_tweet(serializer.validated_data['message'], tweet_id)
            return Response({'status': 'Reply Sent'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserTimelineView(APIView):
    def post(self,request):
        serializer = UsernameSerializer(data=request.data)
        count = request.data.get('count', 10)
        if serializer.is_valid():
            timeline = twitter_service.get_user_timeline(serializer.validated_data['username'], count)
            return Response(timeline, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
