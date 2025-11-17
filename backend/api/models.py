from django.contrib.auth import get_user_model
from django.db import models 


User = get_user_model()

class RequestModel(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    htmldata = models.TextField()


