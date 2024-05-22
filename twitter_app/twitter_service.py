import tweepy

class TwitterService:
    def __init__(self, api_key, api_secret_key,  access_token, access_token_secret):
        auth = tweepy.OAuthHandler(api_key, api_secret_key)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)

    def tweet(self, message):
        self.api.update_status(status=message)

    def get_tweets(self, keyword, count=10):
        tweets = self.api.search(q=keyword, count=count, tweet_mode='extended')
        return [{'text': tweet.full_text, 'user': tweet.user.screen_name} for tweet in tweets]
