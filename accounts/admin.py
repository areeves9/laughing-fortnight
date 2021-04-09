from django.contrib import admin
from accounts.models import SiteUser
# Register your models here.


class SiteUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'last_login',)
    fields = ('headline', 'city', 'about', 'phone', 'skills',)


admin.site.register(SiteUser, SiteUserAdmin)
