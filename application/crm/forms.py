# forms.py
from django import forms
from .models import BussinessCustomer, SwiftApplication

class BusinessCustomerForm(forms.ModelForm):
    class Meta:
        model = BussinessCustomer
        fields = ['first_name', 'last_name', 'phone_number','age', 'email', 'password']

class SwiftApplicationForm(forms.ModelForm):
    class Meta:
        model = SwiftApplication
        fields = ['bank_name','bank_address','account_holder_name',"swift_bic_code","account_number","account_type","currency","country"]
    
class BussinessCustomerLoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = BussinessCustomer
        fields = ['email', 'password']
