from django.db import models
import uuid

from django.contrib.auth.models import User

# Create your models here.

class Manufacturer(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manufacturer_name = models.CharField(max_length=200, unique=True)
    is_active = models.BooleanField(default=True)
    posting_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.manufacturer_name)

class Model(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manufacturer = models.OneToOneField(Manufacturer, on_delete=models.CASCADE)
    model_name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    posting_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.model_name)

class Car(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    title_status = models.CharField(max_length=20)
    build_year = models.IntegerField()
    car_condition = models.CharField(max_length=50)
    cylinders = models.IntegerField()
    fuel = models.CharField(max_length=20)
    odometer = models.IntegerField()
    transmission = models.CharField(max_length=20)
    vin = models.CharField(max_length=30)
    drive = models.CharField(max_length=50)
    car_size = models.CharField(max_length=50)
    car_type = models.CharField(max_length=50)
    paint_color = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    state = models.CharField(max_length=100)
    price = models.IntegerField()
    sold_out = models.BooleanField(default=False)
    selling_price = models.IntegerField()
    purchased_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='purchase_id', null=True, blank=True)
    posting_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.manufacturer) + ' ' +str(self.model)




