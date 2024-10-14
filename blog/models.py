from msilib.schema import ListView
from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class blog (models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='blogs/')
    title= models.CharField (max_length=100)
    description =models.TextField(max_length=1000)
    create_at=models.DateTimeField( auto_now=True)
    category=models.ForeignKey('category',  on_delete=models.CASCADE)
    active =models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title
    
class comment(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey('blog.comment', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField( max_length=50)
    email=models.EmailField( max_length=254)
    write_a_comment=models.TextField(max_length=10000)
    created_at=models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    



    
    

    

    
    

   
    
    
    
   
class category(models.Model):
    title=models.CharField( max_length=50)
    def __str__(self):
        return self.title