from users.models import UserProfile, OAuthService
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
import logging
from calais import Calais
import tweepy
import twitter_settings

# Get an instance of a logger
logger = logging.getLogger(__name__)

#@login_required
def home(request):
    try:
        twitter_handle= request.REQUEST['twitter_handle']
    except BaseException as e:
        twitter_handle="dakoller"
        
    calais = Calais(twitter_settings.CALAIS_API_KEY , submitter="ask-a-sap-question")
    
    auth = tweepy.OAuthHandler(twitter_settings.TWITTER_CONSUMER_TOKEN, twitter_settings.TWITTER_CONSUMER_SECRET)
    auth.set_access_token(twitter_settings.TWEEPY_ACCESS_TOKEN , twitter_settings.TWEEPY_ACCESS_SECRET)
    api = tweepy.API(auth)

    
    
    #if (request.user.is_authenticated() ):        
    return render_to_response('index.html', { 'user_name': 'daniel', 'servicecount': 5 })
    #else:
    #    return render_to_response('index.html')
    