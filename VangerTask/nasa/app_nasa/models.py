from django.db import models
from filer.fields.image import FilerImageField


class Slider(models.Model):
    name = models.CharField(max_length=255)
    image = FilerImageField(null=True, blank=True,
                            related_name="Image", on_delete=models.CASCADE)

    class Meta:
        ordering = ['id']  # просто для примера сортирую по id
