from django.contrib import admin
from django.contrib.admin import ModelAdmin

from . import models


class VersionAdmin(ModelAdmin):
    list_filter = ('test',)

class PageAdmin(ModelAdmin):
    list_filter = ('version',)

class StudentPageAdmin(ModelAdmin):
    list_filter = ('student',)

admin.site.register(models.Student)
admin.site.register(models.Test)
admin.site.register(models.Version, VersionAdmin)
admin.site.register(models.Page, PageAdmin)
admin.site.register(models.StudentPage, StudentPageAdmin)
