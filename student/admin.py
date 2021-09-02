from django.contrib import admin
from .models import StudentProfile


class StdProfile(admin.ModelAdmin):
    list_display = ('user','fullname','wallet_amount')
    list_display_links = ('fullname','user')
    search_fields = ('wallet_amount','fullname','user')


admin.site.register(StudentProfile,StdProfile)