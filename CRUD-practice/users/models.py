from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    name = models.CharField(verbose_name="이름", max_length=4)

    GENDER_CHOICE = [("MALE", "남자"), ("FEMALE", "여자")]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE)
    age = models.PositiveIntegerField(verbose_name="나이", null=True)