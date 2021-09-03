from django.contrib import admin
from .models import TutorProfile


class TutProfile(admin.ModelAdmin):
    list_display = ('user','fullname')
    list_display_links = ('fullname','user')


admin.site.register(TutorProfile,TutProfile)