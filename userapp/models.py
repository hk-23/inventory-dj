from django.db import models

from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
	email = models.EmailField()
	first_name = models.CharField(max_length=50)

	#required during createsuperuser command
	REQUIRED_FIELDS = ['first_name','email']