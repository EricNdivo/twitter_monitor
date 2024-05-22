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
            user_info = {
                'id': user.id_str,
                'name': user.name,
                'screen_name': user.screen_name,
                'location': user.location,
                'description': user.description,
                'followers_count': user.followers_count,
                'friends_count': user.friends_count,
                'statuses_count': user.statuses_count
            }
            return user_info
        except tweepy.TweepyException as e:
            print(f"Error fetching user info: {e}")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None

    def reply_to_tweet(self, mssage, tweet_id):
        try:
            self.api.update_status(status=message, in_reply_to_status_id=tweet_id, auto_populate_reply_metadata=True)
        except tweepy.TweepyException as e:
            print(f"Error: {e}")


    def get_user_timeline(self, username, count=10):
        try:
            tweets = self.api.user_timeline(screen_name=username, count=count, tweet_mode='extended')
            return [{'text': tweet.full_text, 'created_at': tweet.created_at} for tweet in tweets]
        except tweepy.TweepyException as e:
            print(f"Error: {e}")
            return []
