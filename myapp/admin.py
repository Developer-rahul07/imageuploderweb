from django.contrib import admin
from .models import ImageUploder

# Register your models here.
@admin.register(ImageUploder)
class ImageUploderAdmin(admin.ModelAdmin):
    list_display = ['id','photo','date']
