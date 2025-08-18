from django.contrib import admin
from user.models import CustomUser, Address

admin.site.register(CustomUser)
admin.site.register(Address)

# Register your models here.
