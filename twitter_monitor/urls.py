"""
URL configuration for twitter_monitor project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from twitter_app.views import TweetView, MonitorTweetsView, UserInfoView, ReplyTweetView, UserTimelineView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/tweet/', TweetView.as_view(), name='Tweet'),
    path('api/monitor/', MonitorTweetsView.as_view(), name='monitor-tweets'),
    path('api/user_info/',UserInfoView.as_view(), name='user_info'),
    path('api/reply_tweet/', ReplyTweetView.as_view(), name='reply_tweet'),
    path('api/user_timeline/',UserTimelineView.as_view(),name='user_timeline'),
    path('tweet/', TweetView.as_view(), name='tweet'),

]
