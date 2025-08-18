from django.contrib import admin
from service.models.service_model import Service
from user.models import Notification

admin.site.register(Service)
admin.site.register(Notification)
