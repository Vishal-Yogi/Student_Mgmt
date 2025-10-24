from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'roll_no', 'department', 'email',
                    'maths', 'physics', 'chemistry', 'hindi', 'english',
                    'get_total_marks', 'get_percentage', 'get_status')
    search_fields = ('name', 'roll_no', 'department', 'email')
    list_display_links = ('name',)
    actions = ['delete_selected']



    # Computed fields inside the class
    def get_total_marks(self, obj):
        return obj.total_marks
    get_total_marks.short_description = 'Total Marks'

    def get_percentage(self, obj):
        return obj.percentage
    get_percentage.short_description = 'Percentage'

    def get_status(self, obj):
        return obj.status
    get_status.short_description = 'Status'
