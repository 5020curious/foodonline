from django.contrib import admin
from .models import User, UserProfile
from django.contrib.auth.admin import UserAdmin



class CustomUserAdmin(UserAdmin):
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    ordering = ('email',)
    list_display = ('email', 'first_name', 'last_name', 'date_joined')

admin.site.register(User, CustomUserAdmin)

admin.site.register(UserProfile)