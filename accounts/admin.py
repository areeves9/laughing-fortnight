from django.contrib import admin
from accounts.models import SiteUser
# Register your models here.


class SiteUserAdmin(admin.ModelAdmin):
    fields = ('headline', 'city', 'about', 'phone', 'skills',)


admin.site.register(SiteUser, SiteUserAdmin)
