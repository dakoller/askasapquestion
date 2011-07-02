from users.models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import logout
from django.shortcuts import render_to_response
from django.contrib.auth.models import User

def home(request):
    if (request.user.is_authenticated() ):        
        return render_to_response('index.html', { 'user_name': request.user.get_full_name() })
    else:
        return render_to_response('index.html')
    