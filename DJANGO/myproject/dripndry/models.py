from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class dripndry(models.Model):
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	email=models.CharField(max_length=100)
	mobile=models.CharField(max_length=50)

day_choices=(('Mon','MONDAY'),('Tue','TUESDAY'),('Wed','WEDNESDAY'),('Thu','THURSDAY'),('Fri','FRIDAY'),('Sat','SATURDAY'))
slot_choices = (('8.00AM-10.00AM','8.00AM-10.00AM'),('10.00AM-12.00PM','10.00AM-12.00PM'),('1.00PM-3.00PM','1.00PM-3.00PM'),('3.00PM-5.00PM','3.00PM-5.00PM'),('5.00PM-7.00PM','5.00PM-7.00PM'))
cloth_choices = (('Top','Tops'),('Shirt','Shirts'),('Trouser','Trousers'),('Dress','Dresses'),('Sarees','Sarees'),('Baby','Baby items'),('Suit','Suits/Jackets'),('Sock','Socks/Gloves'),('Bed','BedSheets'),('Curtain','Curtains'),('Other','Others'))
urgent_choices=(('yes','yes'),('no','no'))
treatment_choices=(('Wash and Fold','Wash and Fold'),('Wash and Iron','Wash and Iron'),('Dry Cleaning','Dry Cleaning'))


class order(models.Model):
	
	#date     = models.DateField(max_length=10,default="")
	#quantity = models.CharField(max_length=10)
	pickup_day = models.CharField(max_length=50,choices = day_choices,default='MONDAY')
	slot = models.CharField(max_length=50,choices = slot_choices,default='5.00PM-7.00PM')
	immediate_delivery = models.CharField(max_length=50,choices=urgent_choices,default='no')
	cloth = models.CharField(max_length=50,choices = cloth_choices,default='Dress')
	quantity = models.CharField(max_length=10)
	treatment = models.CharField(max_length=50,choices = treatment_choices,default='Wash and Fold')






