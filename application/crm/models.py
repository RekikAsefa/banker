from django.db import models
from django.contrib.auth.models import AbstractUser , User


class ChatSession(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    admin = models.ForeignKey(User, related_name='chat_admin', on_delete=models.CASCADE)
    session_key = models.CharField(max_length=40, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username if self.user else "Anonymous User"} - Admin'

class ChatMessage(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    chat_session = models.ForeignKey(ChatSession, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username if self.user else "Anonymous User"} - {self.timestamp}'

class BussinessCustomer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    email = models.CharField(max_length=200,unique=True)
    password = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)

    def __str__(self): 
        return self.email

class SwiftApplication(models.Model):
    bank_name = models.CharField(max_length=100,default='')
    bank_address = models.CharField(max_length=100,default='')
    swift_bic_code = models.CharField(max_length=20,default='')
    account_holder_name = models.CharField(max_length=100,default='')
    account_number = models.CharField(max_length=50,default='')
    iban = models.CharField(max_length=30,default='',null=True)
    account_type = models.CharField(max_length=20,default='')
    currency = models.CharField(max_length=3,default='')
    country = models.CharField(max_length=2,default='')
    additional_notes = models.TextField(blank=True, null=True)
    owner = models.ForeignKey(BussinessCustomer,on_delete=models.CASCADE)
    STATUS_CHOICES = [
        ('P','Pending'),
        ('A','Approved'),
        ('R','Rejected')
    ]
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='P')

    def __str__(self):
        return f"""{self.owner}-{self.account_number}"""




