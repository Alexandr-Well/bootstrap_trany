from django.db import models


class File(models.Model):
    file = models. ImageField(upload_to='files/%Y/%m/%d')

    def __str__(self):
        return str(self.pk)
