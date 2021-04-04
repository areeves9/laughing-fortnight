from django.contrib import admin
from companies.models import Company, Experience
# Register your models here.


class CompanyAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'email',
        'us_phone',
        'is_licensed',
    )


class ExperienceAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'company',
        'date_from',
        'date_to',
        'description',
        'is_current',
        'user',
    )


admin.site.register(Company, CompanyAdmin)
admin.site.register(Experience, ExperienceAdmin)
