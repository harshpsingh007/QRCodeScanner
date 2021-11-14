from django.contrib import admin
from .models import Scanned

# Register your models here.
@admin.register(Scanned)
class ScannedAdmin(admin.ModelAdmin):
    list_display = ("num",)
    search_fields = ("num",)