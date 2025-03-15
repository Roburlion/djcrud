from django.contrib import admin
from .models import ButtonLog, WOB, Workflow, Roll, RollBatch

admin.site.register(ButtonLog)

admin.site.register(WOB)
admin.site.register(Workflow)
admin.site.register(Roll)
admin.site.register(RollBatch)