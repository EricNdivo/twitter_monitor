import tweepy
from django.conf import settings
class TwitterService:
    def __init__(self, api_key, api_secret_key, access_token, access_token_secret):
        auth = tweepy.OAuthHandler(api_key, api_secret_key)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        try:
            self.api.update_status(status=message)
        except tweepy.TweepyException as e:
            print(f"Error: {e}")
    def get_tweets(self, keyword, count=10):
        try:
            tweets = self.api.search(q=keyword, count=count, tweets_mode='extended')
            return[{'text':tweet.full_text, 'user': tweet.user.screen_name} for tweet in tweets]
        except tweepy.TweepyException as e:
            print(f"Error: {e}") 
            return []
    def get_user_info(self, username):
        try:
            user = self.api.get_user(screen_name=username)
            return {
                'username':user.screen_name,
                'name':user.name,
                'followers_count':user.description,
                'friends_count':user.friends_count,
                'statuses_count':user.statuses_count
            }
        except tweepy.TweepyException as e:
            print(f"Error: {e}")
            return None
            