from django.shortcuts import render_to_response
from calais import Calais
import twitter_settings
import tweepy
from users.models import UserProfile, OAuthService, OAuthAccessData


# Create your views here.
def index(request):
    return render_to_response('events_index.html')
    
def calais_test(request):
    content_url= request.REQUEST['content_url']
    if content_url == '':
        content_url='http://n-tv.de'
    calais = Calais('pc5v39x8sq3mh4mv9zm2ppre' , submitter="ask-a-sap-question")
    result= calais.analyze_url(content_url)
    result.print_summary()
    c_data= {
        "name"  :   "Barack",
    }
    for entity in result.entities:
        c_data[entity['name']]=entity['_type']
    lang= result.doc['meta']['language']
    return render_to_response('calais_test.html',{ 'text': content_url, 'calais_data': c_data, 'language': lang})
    
    
    
    