from django.contrib import admin

# Register your models here.
from .models import Sale, History, Session_Cart

admin.site.register(Sale)
admin.site.register(History)
admin.site.register(Session_Cart)
