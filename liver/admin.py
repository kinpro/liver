from models import *

import logging
logger = logging.getLogger("liver.admin")

from comoda.fileclusters.admin import *
from django import forms
from django.contrib import admin

from django.utils.translation import ugettext_lazy, ugettext as _

def clone(modeladmin, request, queryset):
    for o in queryset:
        o.clone()
clone.short_description = _("Clone")

class RecordRuleInLine(admin.TabularInline):
        model = RecordRule
        extra = 1

class RecordMetadataInLine(admin.TabularInline):
        model = RecordMetadata
        extra = 1

class RecordJobMetadataInLine(admin.TabularInline):
        model = RecordJobMetadata
        extra = 1

class RecordSourceAdmin(admin.ModelAdmin):
    actions = [
            clone,
    ]

    inlines = [
                RecordRuleInLine,
                RecordMetadataInLine,
    ]

    list_display = [
            'source',
            # 'insertion_date',
            'modification_date',
            'enabled',
            'enabled_since',
            'enabled_until',
            'edit_html',
    ]

    list_editable = [
            'source',
            'enabled',
            'enabled_since',
            'enabled_until',

    ]

    list_display_links = ['edit_html']

    list_per_page = 200

    def edit_html(self, queryset):
        return '''<a href="%s/">Edit</a>''' % queryset.id
    edit_html.short_description = ''
    edit_html.allow_tags = True



class RecordJobAdmin(admin.ModelAdmin):
    actions = [
            clone,
    ]

    exclude = ["record_source"]
    readonly_fields = [
            'insertion_date',
            'modification_date',
            'execution_date',
            'completion_date',
    ]

    fieldsets = (
        (None, {
            'fields': (
                (
            'source',
            'scheduled_start_date',
            'scheduled_duration',
                ),

            )
        }),
        (_("Process"), {
            'fields': (
                (
            'status',
            'recorder',
            'result',
                ),
                (
            'insertion_date',
            'modification_date',
            'execution_date',
            'completion_date',
                ),

            )
        }),

    )

    list_filter = [
            "enabled",
            "status",
            "source",
            "recorder",
    ]

    inlines = [
        RecordJobMetadataInLine,
    ]

class SourceAdmin(admin.ModelAdmin):
    actions = [
            clone,
    ]
    ordering = ['name']

    readonly_fields = [
            'insertion_date',
            'modification_date',
    ]

    fieldsets = (
        (None, {
            'fields': (
                (
            'name',
            'external_id',
            'uri',
                ),

            )
        }),
        (None, {
            'fields': (
                (
            'insertion_date',
            'modification_date',
                ),

            )
        }),
        (None, {
            'fields': (
                (
            'default_offset_start',
            'default_offset_end',
            'default_availability_window',
                ),

            )
        }),
    )

class RecorderAdmin(admin.ModelAdmin):
    ordering = ['name','token']

admin.site.register(Source,SourceAdmin)
admin.site.register(Recorder,RecorderAdmin)
admin.site.register(RecordSource,RecordSourceAdmin)
admin.site.register(RecordJob,RecordJobAdmin)

