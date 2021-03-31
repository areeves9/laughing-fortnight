from django.db import models

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
    url = models.URLField(blank=True, null=True)
    is_licensed = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
