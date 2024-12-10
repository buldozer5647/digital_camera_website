from django.db import models
from django.contrib.auth import get_user_model
import uuid
import os

class DigitalImage(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField()
    alt_text = models.CharField(max_length=500)
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to="digital_images/")

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        try:
            old_instance = DigitalImage.objects.get(pk=self.pk)

            self.image.delete(save=True)
            
            super().save(*args, **kwargs)
        except DigitalImage.DoesNotExist:
            super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # if self.image and os.path.isfile(self.image.path):
        #     os.remove(self.image.path)
        self.image.delete(save=True)
        
        super().delete(*args, **kwargs)
