from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


# profile model 
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city =models.ForeignKey("cities", on_delete=models.CASCADE , blank=True,null=True )
    number = models.CharField(max_length=25)
    image = models.ImageField(upload_to='acc/')
    
    
    def __str__(self):
        return str(self.user)
    
    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
    
    
    
class cities(models.Model):
    name=models.CharField(max_length=30)
    def __str__(self):
        return self.name
    