from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.Hour)
admin.site.register(models.Day)
admin.site.register(models.Week)
admin.site.register(models.Month)
admin.site.register(models.Year)


