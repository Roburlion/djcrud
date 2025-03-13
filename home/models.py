# home/models.py
from django.db import models
from django.utils import timezone

class ButtonLog(models.Model):
    pressed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            local_time = timezone.localtime(self.pressed_at)
            return f"{local_time:%Y-%m-%d %H:%M:%S}"

class CustomerAging(models.Model):
    days_old = models.IntegerField()
    batch_id = models.TextField(unique=True)
    mfg_batch_id = models.IntegerField()
    status = models.TextField()
    order_qty = models.IntegerField()
    page_qty = models.IntegerField()

    def __str__(self):
        return f"{self.batch_id}"
