from django.db import models
from django.utils.text import slugify


class Pets(models.Model):
    name = models.CharField(
        max_length=30,
    )

    personal_photo = models.URLField()

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        null=False,
        editable=False,
    )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f'{self.name}-{self.id}')
            super().save(self, *args, **kwargs)



