from django.contrib import admin
from .models import kinder, free, recycle
# Register your models here.

admin.site.register(kinder)
admin.site.register(recycle)
admin.site.register(free)