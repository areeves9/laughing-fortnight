from django.conf import settings
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.urls import reverse

# Create your models here.


class Company(models.Model):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        blank=False,
        null=False,
    )
    name = models.CharField(max_length=255, blank=False, null=False)
    us_phone = PhoneNumberField(blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    is_licensed = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name


class Experience(models.Model):
    FULLTIME = 'full-time'
    PARTIME = 'part-time'
    CONTRACT = 'contract'
    EMPLOYMENT_TYPE = [
        (FULLTIME, 'full-time'),
        (PARTIME, 'part-time'),
        (CONTRACT, 'contract'),
    ]
    company = models.ForeignKey(
        'Company',
        on_delete=models.PROTECT,
    )
    date_from = models.DateField()
    date_to = models.DateField(blank=True, null=True)
    description = models.TextField()
    headline = models.CharField(max_length=255)
    employment_type = models.CharField(
        choices=EMPLOYMENT_TYPE,
        default=FULLTIME,
        max_length=150,
    )
    title = models.CharField(max_length=120)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    is_current = models.BooleanField(default=False)

    class Meta:
        ordering = ('date_from',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('companies:experience-detail', kwargs={'pk': self.pk})
