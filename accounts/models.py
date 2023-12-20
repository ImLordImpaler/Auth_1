from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, **extra_fields):
        if not phone_number:
            raise ValueError("The Phone Number field must be set")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_unusable_password()
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(phone_number, **extra_fields)

class UserModel(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(unique=True, max_length=10)  # Adjust max_length as needed
    name = models.CharField(max_length=60)
    phone_no = models.CharField(max_length=10, null=True , blank=True)
    extra_json = models.TextField(default={})  # Try using model function to always serialize dict before entering any data
    
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser  = models.BooleanField(default=False)
    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def set_password(self, raw_password):
        pass

    def check_password(self, raw_password):
        return True

    def has_usable_password(self):
        return False
    
    def __str__(self):
        return "{} - {}".format(self.name, self.phone_number)



class OTP(models.Model):
    phone = models.CharField(max_length=10)
    otp = models.CharField(max_length=5)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone

