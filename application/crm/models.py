from django.db import models

# Create your models here.
class BussinessCustomer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self): 
        return self.email

class SwiftApplication(models.Model):
    owner = models.ForeignKey(BussinessCustomer,on_delete=models.CASCADE)
    swiftbase_code = models.CharField(max_length=10)


    def __str__(self):
        return self.swiftbase_code


