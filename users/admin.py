#!/usr/bin/env python
from django.contrib import admin
from models import UserProfile, OAuthAccessData, OAuthService

admin.site.register(UserProfile)
admin.site.register(OAuthAccessData)
admin.site.register(OAuthService)
