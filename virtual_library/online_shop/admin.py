from django.contrib import admin

# Register your models here.
from .models import Sale, History

admin.site.register(Sale)
admin.site.register(History)
