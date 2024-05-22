from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TweetSerializer, KeywordSerializer
from .twitter_service import TwitterService
from django.conf import settings

twiter_service = TwitterService(
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
            return Response({'status':'Tweet sent'}, status=status.HTTP_200-OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        