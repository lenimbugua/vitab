import datetime

from django.db import models

from cloudinary.models import CloudinaryField


class Base(models.Model):
    name = models.CharField(max_length=40)
    date_added = models.DateField(auto_now_add=True, default=datetime.datetime.now())
    creator = models.ForeignKey(User, on_delete=Cascade)

    class Meta:
        abstract = True


class Photo(Base):
    image = CloudinaryField()

    def __str__(self):
        return "{}".format(self.image.name)

    def save(self, *args, **kwargs):
        name = super(Photo, self).image.name

        self.save()


class Video(Base):
    pass


class Contest(Base):
    pass
