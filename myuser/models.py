from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils import timezone
from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """ Custom User Instance """

    username = models.CharField(
        "Username", max_length=255, blank=False, unique=True)
    email = models.EmailField("Email", blank=False, unique=True)
    phone = models.CharField("Phone", max_length=17, blank=False, unique=True)
    first_name = models.CharField("First Name", max_length=128, blank=True)
    last_name = models.CharField("Last Name", max_length=128, blank=True)
    bio = models.CharField("Bio", max_length=500, blank=True)
    profile_picture = models.ImageField("Profile Picture",upload_to='media/images/profilePics', blank = True)
    website_url = models.URLField("Website URL",max_length=255, blank=True)
    is_blocked = models.BooleanField("Is Blocked", default=False)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __unicode__(self):
        return self.get_full_name()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self
    
