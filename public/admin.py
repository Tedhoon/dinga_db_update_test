from django.contrib import admin
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from .models import PublicData, PublicUpdate, CascadeTest


class PublicDataAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['pb_name','pb_target_area']

class PublicUpdateAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['pb_name','pb_target_area']

admin.site.register(PublicData, PublicDataAdmin)
admin.site.register(PublicUpdate, PublicUpdateAdmin)
admin.site.register(CascadeTest)