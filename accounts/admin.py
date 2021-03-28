from django.contrib import admin
from accounts.models import SiteUser
# Register your models here.


class SiteUserAdmin(admin.ModelAdmin):
    fields = ('email', 'skills',)


admin.site.register(SiteUser, SiteUserAdmin)
