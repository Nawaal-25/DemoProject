from django.contrib import admin
from .models import Register

# Register your models here.
@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'uemail')  # Display these fields in the admin panel
    search_fields = ('username', 'uemail')      # Add search functionality for these fields
    list_filter = ('uemail',)                   # Add filter options based on email
