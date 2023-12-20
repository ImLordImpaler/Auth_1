from django.urls import path 
from .views import * 


'''
login:
    1) POST -> Takes phone number -> Sends OTP 
    2) login_check -> Enters OTP -> Returns Token 

signup
    1) POST -> Takes user's data and creates a token and user 
'''


urlpatterns = [
    path('send_otp', AuthView.as_view({'post': 'send_otp'})),
    path('check_otp',  AuthView.as_view({'post': 'check_otp'})),

    path('login', AuthView.as_view({'post':'login_func'})),
    path('register', AuthView.as_view({'post':'register_user'}))
]