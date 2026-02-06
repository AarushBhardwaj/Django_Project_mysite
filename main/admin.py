from django.contrib import admin
from .models import Tutorial, TutorialCategory, TutorialSeries, ContactMessage

# Register your models here.


class TutorialAdmin(admin.ModelAdmin):
	fieldsets = [
			("Title/Date", {"fields": ["tutorial_title", "tutorial_published"]}),
			("URL", {"fields": ["tutorial_slug"]}),
			("Series", {"fields": ["tutorial_series"]}),
			("Content", {"fields": ["tutorial_content"]})
	]
	list_display = ['tutorial_title', 'tutorial_series', 'tutorial_published']
	search_fields = ['tutorial_title', 'tutorial_content']


class TutorialCategoryAdmin(admin.ModelAdmin):
	list_display = ['tutorial_category', 'category_summary', 'category_slug']


class TutorialSeriesAdmin(admin.ModelAdmin):
	list_display = ['tutorial_series', 'tutorial_category', 'series_summary']


class ContactMessageAdmin(admin.ModelAdmin):
	list_display = ['subject', 'name', 'email', 'created_at', 'is_read']
	list_filter = ['is_read', 'created_at']
	search_fields = ['name', 'email', 'subject', 'message']
	readonly_fields = ['name', 'email', 'subject', 'message', 'created_at']


admin.site.register(TutorialCategory, TutorialCategoryAdmin)
admin.site.register(TutorialSeries, TutorialSeriesAdmin)
admin.site.register(Tutorial, TutorialAdmin)
admin.site.register(ContactMessage, ContactMessageAdmin)

