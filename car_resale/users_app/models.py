from django.db import models
import uuid

from django.contrib.auth.models import User
from car_app.models import Car

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    profile_image = models.ImageField(null=True, blank=True, upload_to='profiles/', default="profiles/default_profile_photo.jpg")
    date_of_birth = models.DateField()
    addr_1 = models.CharField(max_length=100, null=True, blank=True)
    addr_2 = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(choices=(('MH', 'Maharashtra'),('GJ', 'Gujarat')), null=True, blank=True)
    zip_code = models.CharField(max_length=6 ,null=True, blank=True)
    country = models.CharField(default='India', editable=False)
    contact = models.CharField(max_length=10, null=True, blank=True)
    user_type = models.CharField(default='Customer', choices=(('Staff','Staff'),('Customer','Customer')))

    def __str__(self):
        return str(self.user)

    @property
    def imageURL(self):
        try:
            url = self.profile_image.url
        except:
            url = ''
        return url
    
class Wishlist(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    posting_date = models.DateTimeField(auto_now_add=True)
    


    