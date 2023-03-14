from django.contrib import admin

from feedback.models import Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_text', 'created_on', 'status_processing')
    list_editable = ("status_processing",)
    fields = ('name', 'mail', 'text', 'created_on', 'status_processing')

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False
