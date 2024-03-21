from django.contrib import admin
from django_filters import rest_framework as filters
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','phone_number', 'first_name', 'type', 'market')
    list_filter = ['phone_number', 'market']
