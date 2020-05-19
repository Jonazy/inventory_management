from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Inventory)
class AdminView(admin.ModelAdmin):
    pass
