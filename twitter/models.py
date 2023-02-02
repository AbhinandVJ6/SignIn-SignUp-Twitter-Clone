from django.db import models

# Create your models here.
from django.db import models
from cloudinary.models import CloudinaryField
# from cloudinary.model import cloudinaryField


class Tweet(models.Model):
    class Meta(object):
        db_table = 'post'

    body = models.CharField(
        'Body', blank=True, null=True, max_length=140, db_index=True
    )
    created_at = models.DateTimeField(
        'Created DateTime', blank=True, auto_now_add=True
    )
    image = CloudinaryField(
        'image',blank=True, db_index=True
    )
    likes = models.PositiveBigIntegerField(
        'likes', default=0, null=True, blank=True
    )
