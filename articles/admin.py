from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.articles)
admin.site.register(models.read_info)
admin.site.register(models.starred_info)