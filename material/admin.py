from django.contrib import admin
from .models import Course, Department,Material, PastQuestion, Time, Day, LectureHour, TimeTable, DepartmentRepresentative,Announcement
# Register your models here.

admin.site.register(Material)
admin.site.register(Course)
admin.site.register(DepartmentRepresentative)
admin.site.register(PastQuestion)
admin.site.register(Department)
admin.site.register(TimeTable)
admin.site.register(Time)
admin.site.register(Day)
admin.site.register(LectureHour)

# Isah @££%^£ material/admin.py
from django.contrib import admin
from .models import (
    Material, Department, Course, PastQuestion, 
    TimeTable, DepartmentRepresentative,
    Bulletin, AcademicEvent  # ADD THE NEW MODELS HERE
)

# ... your existing admin registrations ...

# ADD THESE NEW ADMIN REGISTRATIONS
@admin.register(Bulletin)
class BulletinAdmin(admin.ModelAdmin):
    list_display = ['title', 'is_active', 'created_at']
    list_filter = ['is_active', 'created_at']
    search_fields = ['title', 'description']
    list_editable = ['is_active']

@admin.register(AcademicEvent)
class AcademicEventAdmin(admin.ModelAdmin):
    list_display = ['title', 'event_type', 'start_date', 'end_date', 'is_important']
    list_filter = ['event_type', 'is_important', 'start_date']
    search_fields = ['title', 'description']
    list_editable = ['is_important']
    
 

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ['title', 'priority', 'is_active', 'created_at', 'created_by', 'has_image']
    list_filter = ['priority', 'is_active', 'created_at']
    search_fields = ['title', 'content']
    list_editable = ['is_active', 'priority']
    
    # ADD FIELDSETS FOR BETTER ORGANIZATION
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'content', 'image')
        }),
        ('Settings', {
            'fields': ('priority', 'is_active')
        }),
    )
    
    def save_model(self, request, obj, form, change):
        if not obj.pk:  # If creating new announcement
            obj.created_by = request.user
        super().save_model(request, obj, form, change)
    
    # ADD THIS METHOD TO SHOW IMAGE THUMBNAIL IN LIST
    def has_image(self, obj):
        return bool(obj.image)
    has_image.boolean = True
    has_image.short_description = 'Has Image'