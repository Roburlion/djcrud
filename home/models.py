# home/models.py
from django.db import models
from django.utils import timezone

class ButtonLog(models.Model):
    pressed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
            local_time = timezone.localtime(self.pressed_at)
            return f"{local_time:%Y-%m-%d %H:%M:%S}"
    
    class Meta:
        verbose_name = "Button Log"
        verbose_name_plural = "Button Logs"

class WOB(models.Model):
    wob = models.CharField(max_length=32, primary_key=True)
    batch = models.CharField(max_length=9, blank=True, null=False, default='')
    status = models.CharField(max_length=64, blank=False, null=False, default='Other')
    age = models.IntegerField(null=False)
    order_qty = models.IntegerField()
    page_qty = models.IntegerField()
    uploaded_at = models.DateTimeField()

    class Meta:
        verbose_name = "WOB"
        verbose_name_plural = "WOBs"
        indexes = [models.Index(fields=['batch', 'age', 'uploaded_at'])]

    def __str__(self):
        local_time = timezone.localtime(self.uploaded_at)
        return f"wob: {self.wob}, batch: {self.batch}, status: {self.status}, age: {self.age}, order_qty: {self.order_qty}, page_qty: {self.page_qty}, uploaded_at: {local_time:%Y-%m-%d %H:%M:%S}"

class Workflow(models.Model):
    workflow = models.CharField(primary_key=True, max_length=16)
    name = models.TextField(unique=True, blank=False, null=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"workflow: {self.workflow}, name: {self.name}, deleted: {self.deleted}"

class Roll(models.Model):
    roll = models.IntegerField(primary_key=True)
    workflow = models.ForeignKey(Workflow, on_delete=models.PROTECT, related_name='roll')
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        local_time = timezone.localtime(self.created_on)
        return f"roll: {self.roll}, workflow: {self.workflow}, created_on: {local_time:%Y-%m-%d %H:%M:%S}"

class RollBatch(models.Model):
    roll = models.ForeignKey(Roll, on_delete=models.PROTECT, related_name='roll_batches')
    batch = models.IntegerField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Roll Batch"
        verbose_name_plural = "Roll Batches"
        unique_together = ('roll', 'batch')

    def __str__(self):
        local_time = timezone.localtime(self.created_on)
        return f"roll: {self.roll}, batch: {self.batch}, created_on: {local_time:%Y-%m-%d %H:%M:%S}"
