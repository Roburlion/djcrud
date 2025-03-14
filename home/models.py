# home/models.py
from django.db import models
from django.utils import timezone

class ButtonLog(models.Model):
    pressed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            local_time = timezone.localtime(self.pressed_at)
            return f"{local_time:%Y-%m-%d %H:%M:%S}"

class WOBs(models.Model):
    wob = models.TextField(unique=True)
    batch = models.IntegerField(null=True)
    status = models.TextField()
    age = models.IntegerField()
    order_qty = models.IntegerField()
    page_qty = models.IntegerField()
    uploaded_at = models.DateTimeField()

    def __str__(self):
        return f"wob: {self.wob}, batch: {self.batch}, status: {self.status}, age: {self.age}, order_qty: {self.order_qty}, page_qty: {self.page_qty}"

class Workflow(models.Model):
    workflow = models.CharField(primary_key=True, max_length=16)
    name = models.TextField()
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"workflow: {self.workflow}, name: {self.name}, deleted: {self.deleted}"

class Rolls(models.Model):
    roll = models.IntegerField(primary_key=True)
    workflow = models.ForeignKey(Workflow, on_delete=models.PROTECT, related_name='rolls')
    created_on = models.DateTimeField()

    def __str__(self):
        return f"roll: {self.roll}, workflow: {self.workflow}, created_on: {self.created_on}"

class RollBatches(models.Model):
    roll = models.ForeignKey(Rolls, on_delete=models.PROTECT, related_name='roll_batches')
    batch = models.IntegerField()
    created_on = models.DateTimeField()

    class Meta:
        unique_together = ('roll', 'batch')

    def __str__(self):
        return f"roll: {self.roll}, batch: {self.batch}, created_on: {self.created_on}"
