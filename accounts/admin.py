from django.contrib import admin

from .models import *
from rest_framework.authtoken.models import Token
admin.site.register(UserModel)
admin.site.register(OTP)