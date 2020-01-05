from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(null=True)

    verification_code = models.IntegerField(default=0)
    code_expiry_date = models.DateTimeField(null=True)
    is_email_verified = models.BooleanField(default=False)

    security_question = models.CharField(max_length=100, null=True)
    security_answer = models.CharField(max_length=100, null=True)
