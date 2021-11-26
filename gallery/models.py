from django.db import models
from cloudinary.models import CloudinaryField


class photos(models.Model):
     #image field
    image_name= CloudinaryField('image')
    # title field
    image_title = models.CharField(max_length=100)
    image_description = models.TextField(max_length=100)

   