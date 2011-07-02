from django.db import models
from django.utils.encoding import smart_str
from django.contrib.auth.models import User

class OAuthService(models.Model):
    name = models.TextField()
    
    def __str__(self):
        return u'%s (OAuthService)' % (self.name)

class OAuthAccessData(models.Model):
    service = models.ForeignKey(OAuthService)
    access_token= models.CharField(max_length= 100)
    access_secret= models.CharField(max_length= 100)
    
    def __str__(self):
        return u'OAuthData for service  %s' % (self.service.name)
    

class UserProfile(models.Model):
    # This is the only required field
    user = models.ForeignKey(User, unique=True, primary_key= True)
    
    oauth_accessdata= models.ManyToManyField(OAuthAccessData, null= True)

    # The rest is completely up to you...
    def __str__(self):
        return u'Userprofile of  %s' % (self.user)
        
User.profile = property(lambda u: UserProfile.objects.get_or_create(user=u)[0])
    