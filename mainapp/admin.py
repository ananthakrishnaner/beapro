from django.contrib import admin
from .models import ContactForm
# Register your models here.



class Contact(admin.ModelAdmin):
    list_display = ('name','email','subject','user_id')
    list_display_links = ('name','email')
    search_fields = ('name','email')


admin.site.register(ContactForm,Contact)