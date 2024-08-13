from django.contrib import admin
from .models import Course
from school_management_system.utils import ExportCsvMixin

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin, ExportCsvMixin):
    """Admin Display Options to manage Course data in the admin panel"""

    list_display = (
        'course_code',
        'course_name',
        'course_description',
        'date_created',
        'status'
    )

    search_fields = (
        'course_name',
        'course_code',
    )

    list_filter = (
        'status',
        'date_created',
    )

    actions = [
        'export_as_csv',
        'activate_courses',
        'deactivate_courses',
    ]

    def activate_courses(self, request, queryset):
        """Activate selected courses."""
        queryset.update(status=True)
        self.message_user(request, "Selected courses have been activated.")

    def deactivate_courses(self, request, queryset):
        """Deactivate selected courses."""
        queryset.update(status=False)
        self.message_user(request, "Selected courses have been deactivated.")

    activate_courses.short_description = "Activate selected courses"
    deactivate_courses.short_description = "Deactivate selected courses"

