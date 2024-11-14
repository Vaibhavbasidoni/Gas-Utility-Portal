from django.contrib import admin
from .models import ServiceRequest, RequestComment

class RequestCommentInline(admin.TabularInline):
    model = RequestComment
    extra = 1  # Number of empty forms to display
    fields = ('staff_name', 'comment', 'created_at')
    readonly_fields = ('created_at',)

@admin.register(ServiceRequest)
class ServiceRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_name', 'request_type', 'status', 'created_at', 'updated_at')
    list_filter = ('status', 'request_type', 'created_at')
    search_fields = ('customer_name', 'customer_email', 'description')
    readonly_fields = ('created_at', 'updated_at')
    inlines = [RequestCommentInline]
    
    fieldsets = (
        ('Customer Information', {
            'fields': ('customer_name', 'customer_email')
        }),
        ('Request Details', {
            'fields': ('request_type', 'description', 'attachment')
        }),
        ('Status Information', {
            'fields': ('status', 'created_at', 'updated_at', 'resolved_at')
        }),
    )

    def save_model(self, request, obj, form, change):
        if 'status' in form.changed_data and obj.status == 'RESOLVED' and not obj.resolved_at:
            obj.resolve()
        super().save_model(request, obj, form, change)

@admin.register(RequestComment)
class RequestCommentAdmin(admin.ModelAdmin):
    list_display = ('service_request', 'staff_name', 'created_at')
    list_filter = ('staff_name', 'created_at')
    search_fields = ('staff_name', 'comment')
    readonly_fields = ('created_at',)