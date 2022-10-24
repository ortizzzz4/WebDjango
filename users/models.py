from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import User




# Create your models here.

class User (AbstractUser):
    
    customer_id=models.CharField(max_length=100, blank=True, null=True)
    
    def get_full_name(self):
         return '{}-{}'.format(self.first_name, self.last_name)
     
class Customer (User):
    class Meta:
        proxy=True
        
    def get_products(self):
        return []#self.product_set.all()
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()