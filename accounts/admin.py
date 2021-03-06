from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account
from django.utils.html import format_html
# Register your models here.


class AccountAdmmin(UserAdmin):
    def profile_photo(self, objects):
        return format_html('<img src="{}" width="40"/>'.format(objects.profile_image.url))

    list_display = ('profile_photo','email','username','date_joined','last_login','is_tutor','is_student')
    search_fields = ('email','username')
    readonly_fields = ('id','date_joined','last_login')
    filter_horizontal = ()
    list_display_links = ('email','username')
    list_filter =('is_admin','is_tutor','is_student')
    fieldsets = ()


admin.site.register(Account,AccountAdmmin)

