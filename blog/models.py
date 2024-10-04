from django.db import models

# Create your models here.

class blog (models.Model):
    image=models.ImageField(upload_to='blogs/')
    description =models.TextField(max_length=1000)
    create_at=models.DateTimeField( auto_now=True)
    category=models.ForeignKey('category',  on_delete=models.CASCADE)
   
    
    
    
   
class category(models.Model):
    title=models.CharField( max_length=50)
    def __str__(self):
        return self.title