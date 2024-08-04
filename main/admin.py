from django.contrib import admin
from . import models

admin.site.register(models.Contact)
admin.site.register(models.ChooseItem)
admin.site.register(models.TeamMember)
admin.site.register(models.Partner)