from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
JOB_TYPE=(
  ('FULL TIME','FULL TIME'),
  ('PART TIME','PART TIME'),  
)



# Create your models here.
#job's class
class job(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=30)
    description=models.TextField(max_length=10000)
    Published_on=models.DateTimeField( auto_now=True)
    vacancy=models.IntegerField(default=1)
    Salary =models.IntegerField(default=1)
    Job_Nature=models.CharField(max_length=50,choices=JOB_TYPE)
    category =models.ForeignKey('category',on_delete=models.CASCADE)
    image = models.ImageField( upload_to='jobs/')
    slug= models.SlugField(blank=True,null=True)  

    
    
    def __str__(self):
        return self.title
    
    
      
    def save (self,*args,**kwargs):
        self.slug=slugify(self.title)
        super(job,self).save(*args,**kwargs)


#job's category class
class category(models.Model):
    title=models.CharField( max_length=50)
    def __str__(self) :
        return self.title

#apply form class
class apply(models.Model):
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    job=models.ForeignKey(job, related_name='apply_job', on_delete=models.CASCADE)
    name=models.CharField( max_length=50)
    email=models.EmailField(max_length=254)
    website=models.URLField(max_length=200)
    cv=models.FileField(upload_to='apply/')
    coverletter=models.TextField(max_length=1000)
    
    def __str__ (self):
        return self.name