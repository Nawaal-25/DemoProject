from django.db import models

# Create your models here.
class Register(models.Model):
    # username=models.CharField(max_length=100)
    username = models.CharField(max_length=255, unique=True)
    uemail=models.EmailField()
    upassword = models.CharField(max_length=255)
    # upassword=models.CharField(max_length=120)



    def __str__(self):
        return self.username