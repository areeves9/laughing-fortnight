from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Company(models.Model):
    chief_executive_officer = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )
    name = models.CharField(max_length=255, blank=False, null=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        blank=False,
        null=False,
    )
    us_phone = PhoneNumberField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    is_licensed = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Experience(models.Model):
    FULLTIME = 'full-time'
    PARTIME = 'part-time'
    CONTRACT = 'contract'
    EMPLOYMENT_TYPE = [
        (FULLTIME, 'full-time employment'),
        (PARTIME, 'part-time employment'),
        (CONTRACT, 'contract'),
    ]
    company = models.ForeignKey('Company', on_delete=models.PROTECT)
    date_from = models.DateField()
    date_to = models.DateField(blank=True, null=True)
    description = models.TextField()
    employment_type = models.CharField(
        choices=EMPLOYMENT_TYPE,
    )
    title = models.CharField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    is_current = models.BooleanField()


class Meta:
    ordering = ('date_from',)


def __str__(self):
    return f'{self.title}, {self.company}'
