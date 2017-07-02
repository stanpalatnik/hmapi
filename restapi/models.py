from django.db import models
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError


def validate_isbn(value):
    if len(value) != 10 and len(value) != 13:
        raise ValidationError(
            "ISBN must be either 10 or 13 characters in length"
        )


class Book(models.Model):
    title = models.CharField(max_length=255, blank=False)
    author = models.CharField(max_length=255, blank=False)
    isbn = models.CharField(max_length=13, blank=False, validators=[validate_isbn])
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=False,
                                validators=[MinValueValidator(0.01)])
    description = models.TextField(blank=True)

    class Meta:
        ordering = ('title',)
