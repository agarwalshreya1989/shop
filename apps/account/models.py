from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.db import models
from django.core.mail import send_mail
from django.conf import settings

# Create your models here.
GENDER = (
    ('M', 'Male'),
    ('F', 'Female')
)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    about_user = models.CharField(max_length=250, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=50)
    # email_verified = models.BooleanField(default=False)
    objects = UserManager()
    

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __unicode__(self):
        return self.get_full_name()

    def get_full_name(self):
        return ''.join(filter(None, [self.first_name, self.last_name])) or self.username

    def get_short_name(self):
        return self.first_name or self.username

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])


class EmailVerification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    token = models.CharField(max_length=100)
    created_on = models.DateTimeField(blank=True, null=True, auto_now_add=True, editable=False)
    # verified = models.BooleanField(default=False)