from django.contrib import admin
from .models import TutorProfile


class TutProfile(admin.ModelAdmin):
    list_display = ('user','fullname','verified','featured')
    list_display_links = ('fullname','user')
    list_filter = ('verified',)
    search_fields = ('fullname',)


admin.site.register(TutorProfile,TutProfile)