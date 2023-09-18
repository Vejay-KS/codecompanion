from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Codecompaniontest(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.title
    

ROLE_CHOICES = (("SoftwareDeveloper","Software Developer"), 
			("SoftwareDevelopmentManager","Software Development Manager"),
			("HumanResourceManager","Human Resource Manager"))

class CodeCompanionUser(AbstractUser):
    username = models.CharField(max_length=50, unique=True)
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    password1=models.CharField(max_length=200)
    password2=models.CharField(max_length=200)
    email = models.EmailField()

    role = models.CharField(
        max_length=200,
        choices = ROLE_CHOICES,
        default = 'SoftwareDeveloper'
        )
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [password1, password2, email, role]