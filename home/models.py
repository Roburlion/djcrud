# home/models.py
from django.db import models
from django.utils import timezone

class ButtonLog(models.Model):
    pressed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            local_time = timezone.localtime(self.pressed_at)
            return f"{local_time:%Y-%m-%d %H:%M:%S}"


# Create your models here.
# class Banner(models.Model):
#     title = models.CharField(max_length=200)
#     image = models.ImageField(upload_to='banners/')
#     description = models.TextField()

#     def __str__(self):
#         return self.title