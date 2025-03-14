# home/models.py
from django.db import models
from django.utils import timezone

class ButtonLog(models.Model):
    pressed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            local_time = timezone.localtime(self.pressed_at)
            return f"{local_time:%Y-%m-%d %H:%M:%S}"

class CustomerAging(models.Model):
    wob = models.TextField(unique=True)
    batch = models.IntegerField(null=True)
    status = models.TextField()
    age = models.IntegerField()
    order_qty = models.IntegerField()
    page_qty = models.IntegerField()
    uploaded_at = models.DateTimeField()

    def __str__(self):
        return f"wob: {self.wob}, batch: {self.batch}, status: {self.status}, age: {self.age}, order_qty: {self.order_qty}, page_qty: {self.page_qty}"
