from django.contrib import admin
from .models import BussinessCustomer, SwiftApplication ,ChatMessage , ChatSession

@admin.register(BussinessCustomer)
class BussinessCustomerAdmin(admin.ModelAdmin):
    list_display = ("email","first_name","last_name","age")
    list_filter = ("email","first_name","last_name")
    search_fields = ("email__startswith","first_name__startswith","last_name__startswith", )
    pass

@admin.register(SwiftApplication)
class SwiftApplicationAdmin(admin.ModelAdmin):
    list_display = ("bank_name","bank_address","account_holder_name","account_number")
    list_filter = ("bank_name","bank_address","account_holder_name","account_number")
    search_fields = ("bank_name__startswith","account_holder_name__startswith" )
    pass

@admin.register(ChatSession)
class ChatSessionAdmin(admin.ModelAdmin):
    list_display = ("user","admin","session_key","timestamp")
    pass

@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ("chat_session","content","user","timestamp")
    # search_fields = ("chat_session__startswith",)
    pass