import datetime

from django.contrib.auth.models import User
from django.db import models

from cloudinary.models import CloudinaryField


class Base(models.Model):
    date_added = models.DateField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Photo(Base):
    image = CloudinaryField()
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return "{}".format(self.image.public_id)
