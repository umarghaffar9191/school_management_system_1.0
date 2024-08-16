import csv
from django.http import HttpResponse

class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        """Export selected items as CSV."""
        meta = self.model._meta
        field_names = [field.name for field in meta.fields if not field.name.endswith('_id')]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename={self.model._meta.model_name}.csv'
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            writer.writerow([getattr(obj, field) if getattr(obj, field) is not None else '' for field in field_names])

        return response

    export_as_csv.short_description = 'Export Selected'
