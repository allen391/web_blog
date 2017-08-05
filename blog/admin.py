from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Article)
admin.site.register(models.Category)
admin.site.register(models.Comments)
admin.site.register(models.ThumbUp)
admin.site.register(models.UserGroup)
admin.site.register(models.UserProfile)

