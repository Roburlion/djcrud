from django.contrib import admin
from .models import ButtonLog, WOBs, Workflow, Rolls, RollBatches
admin.site.register(ButtonLog)

@admin.register(WOBs)
class WOBsAdmin(admin.ModelAdmin):
    verbose_name_plural = "WOBs"  # Ensures it displays as "WOBs" instead of "Wo bss"

admin.site.register(Workflow)
admin.site.register(Rolls)
admin.site.register(RollBatches)