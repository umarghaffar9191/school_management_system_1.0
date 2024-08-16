from django.contrib import admin
from .models import Student , StudentFee
from .forms import StudentAdminForm 

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin ):
    form = StudentAdminForm
    list_display=(
        'id','first_name','last_name',
        'gender','date_of_birth','addmission_date',
        'address','email','phone_number',
        'emergency_contact_phone','current_class',
        'status'
    
    )

    # search_fields = (
    #     'id',
    #     'gender',
    #     'addmission_date',
    # )

    list_filter = (
        'gender',
        'status',

    )

    ordering = ('id',)

@admin.register(StudentFee)
class StudentFeeAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'valid_until',
        'total_amount',
        'date_submitted',
        'receipt_generated',
    )

    actions = ['generate_receipt']



    def generate_receipt(self, request, queryset):
        """Action to generate receipts for selected fees."""
        for fee in queryset:
            fee.generate_receipt()
        self.message_user(request, "Receipts have been generated and sent.")
    generate_receipt.short_description = "Generate Receipt"