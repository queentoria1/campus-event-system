from django.contrib import admin
from .models import Student, Course, Score

@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    # This adds clean, sortable columns to your list view
    list_display = ('student', 'course', 'score')
    
    # This adds an interactive search bar at the top of the page
    search_fields = ('student__first_name', 'student__last_name', 'course__name')

# Register your other models normally if you haven't already
admin.site.register(Student)
admin.site.register(Course)