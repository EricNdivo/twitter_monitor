from django.urls import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from unittest.mock import patch
from .twitter_service import TwitterService

class PostTweetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('tweet')

    def test_post_tweet_valid(self):
        data = {'message': 'This is a valid tweet message'}
        with patch.object(TwitterService, 'post_tweet', return_value={'status': 'success'}) as mock_post_tweet:
            response = self.client.post(self.url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data['message'], 'Tweet posted successfully!')
            mock_post_tweet.assert_called_once_with('This is a valid tweet message')

    def test_post_tweet_invalid(self):
        data = {'message': 'Short'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('message', response.data)
        self.assertIn('Ensure this field has at least 20 characters.', response.data['message'][0])

class UserInfoTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('user_info')
        self.api_key = 'fake_api_key'
        self.api_secret_key = 'fake_api_secret_key'
        self.access_token = 'fake_access_token'
        self.access_token_secret = 'fake_access_token_secret'
        self.twitter_service = TwitterService(
            api_key=self.api_key,
            api_secret_key=self.api_secret_key,
            access_token=self.access_token,
            access_token_secret=self.access_token_secret
        )

    def test_get_user_info_valid(self):
        data = {'username': 'validuser'}
        expected_response = {
            'username': 'validuser',
            'name': 'Valid User',
            'followers_count': 100,
            'following_count': 50,
            'tweets_count': 200,
            'profile_image_url': 'http://example.com/profile.jpg'
        }
        with patch.object(TwitterService, 'get_user_info', return_value=expected_response) as mock_get_user_info:
            response = self.client.post(self.url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, expected_response)
            mock_get_user_info.assert_called_once_with('validuser')

    def test_get_user_info_invalid(self):
        data = {'username': 'nonexistentuser'}
        with patch.object(TwitterService, 'get_user_info', return_value=None) as mock_get_user_info:
            response = self.client.post(self.url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
            self.assertEqual(response.data['error'], 'User not found or other error occurred.')
            mock_get_user_info.assert_called_once_with('nonexistentuser')

class UserTimelineTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('user_timeline')
        self.api_key = 'fake_api_key'
        self.api_secret_key = 'fake_api_secret_key'
        self.access_token = 'fake_access_token'
        self.access_token_secret = 'fake_access_token_secret'
        self.twitter_service = TwitterService(
            api_key=self.api_key,
            api_secret_key=self.api_secret_key,
            access_token=self.access_token,
            access_token_secret=self.access_token_secret
        )

    def test_get_user_timeline_valid(self):
        data = {'username': 'validuser'}
        expected_response = [
            'tweet1',
            'tweet2',
            'tweet3'
        ]
        with patch.object(TwitterService, 'get_user_timeline', return_value=expected_response) as mock_get_user_timeline:
            response = self.client.post(self.url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_200_OK)
            self.assertEqual(response.data, expected_response)
            mock_get_user_timeline.assert_called_once_with('validuser', 10)  # Adjusting for second argument

    def test_get_user_timeline_invalid(self):
        data = {'username': 'nonexistentuser'}
        with patch.object(TwitterService, 'get_user_timeline', return_value=None) as mock_get_user_timeline:
            response = self.client.post(self.url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
            self.assertEqual(response.data['error'], 'User not found or other error occurred.')
            mock_get_user_timeline.assert_called_once_with('nonexistentuser', 10)  # Adjusting for second argument
