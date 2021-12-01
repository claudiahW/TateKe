from django.db import models
from cloudinary.models import CloudinaryField


class photos(models.Model):
     
    image= CloudinaryField('image')
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.title

    def save_image(self):
        self.save()
        
    @classmethod
    def all_images(cls):
            pictures=cls.objects.all()
            return pictures    

   