from django.contrib import admin

# Register your models here.
# from .models import Banner
# admin.site.register(Banner)
from .models import ButtonLog, CustomerAging
admin.site.register(ButtonLog)
admin.site.register(CustomerAging)