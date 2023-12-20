from rest_framework.generics import ListCreateAPIView
from .models import * 
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.authtoken.models import Token
import random
from datetime import datetime


class AuthView(viewsets.ViewSet):
    def send_otp(self , request , **kwargs):
        try:
            phone = request.data['phone']
            otp = str(random.randint(10000, 99999))
            '''
            Check if OTP with user exists, if yes then update the created and OTP
                else, New Entry
            '''
            # otp = OTP.objects.create(phone=phone,otp=otp)
            otp_obj,created = OTP.objects.get_or_create(phone = phone)
            otp_obj.otp = otp
            msg = "OTP created"
            if not created:
                otp_obj.created = datetime.now() 
                msg = "OTP Updated"

            otp_obj.save()
            return Response({'message':msg, 'otp': otp_obj.otp})
        except Exception as E:
            return Response(status=400 , data = {"error_message": str(E)})

    def check_otp(self , request, **kwargs):
        try:
            otp = request.data['otp']
            phone  = request.data['phone']
            otp_obj = OTP.objects.filter(phone = phone, otp=otp).first() 
            
            if not otp_obj:
                raise Exception("OTP verification failed")

            return Response({'data':"Wokring"})
        except Exception as E:
            return Response(status=400 , data = {"error_message": str(E)})
    

    def login_func(cls, request):
        '''
        Internally call Send OTP function 
        Input:{
            "phone_no":""
        }

        -> Check if any user with phone number 
        -> Send OTP to the Phone Number 
        '''
        try:

            return Response({'message':"Login User ENDPOINT"})
        except Exception as E:
            return Response(status=400 , data = {"error_message": str(E)}) 
    def register_user(self, request, **kwargs):
        try:
            '''
            Input: {
                "Name": "",
                "Phone": ""
            }
            
            -> CHeck if user with same number exists. 
            -> Create a new user and token 
            '''

            name = request.data['name']
            phone = request.data['phone']

            if not len(phone)==10:
                raise Exception("Phone number must be of length 10")
            
            user,created = UserModel.objects.get_or_create(phone_number=phone)
            if not created:
                raise Exception("Phone number already registered")
            token = Token.objects.create(user = user)

            return Response({'message': "Register User ENDPOINT", 'token-key': token.key, 'user-data': user.phone_number})
        except Exception as E:
            return Response(status=400 , data = {"error_message": str(E)})