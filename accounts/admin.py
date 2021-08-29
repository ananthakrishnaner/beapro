from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from accounts.models import Account
from django.utils.html import format_html
# Register your models here.


class AccountAdmmin(UserAdmin):
    def profile_photo(self, objects):
        return format_html('<img src="{}" width="40"/>'.format(objects.profile_image.url))

    list_display = ('email','username','profile_photo','date_joined','last_login','is_admin','is_staff')
    search_fields = ('email','username')
    readonly_fields = ('id','date_joined','last_login')
    filter_horizontal = ()
    list_filter =()
    fieldsets = ()


admin.site.register(Account,AccountAdmmin)

