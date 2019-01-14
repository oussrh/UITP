from django.contrib import admin

from . import models
# Register your models here.

admin.site.register(models.UserProfile)
# admin.site.register(models.StatusUpdate)
# admin.site.register(models.Message)
admin.site.register(models.Rapports)
admin.site.register(models.Transports)
admin.site.register(models.TypeIncidents)
admin.site.register(models.Incidents)
admin.site.register(models.Detail)
