from django.contrib import admin
from .models import StudentProfile,StudentTransaction,Coincheck


class StdProfile(admin.ModelAdmin):
    list_display = ('user','fullname','wallet_amount','account_verified')
    list_display_links = ('fullname','user')
    list_filter = ('account_verified',)
    search_fields = ('wallet_amount','fullname','user')

class CoincheckS(admin.ModelAdmin):
    list_display = ('name','coindate',)
    list_display_links = ('name','coindate')


class Transaction(admin.ModelAdmin):
    list_display = ('fullname','amount','created','paid')
    list_filter = ('paid',)

admin.site.register(StudentTransaction,Transaction)
admin.site.register(Coincheck,CoincheckS)
admin.site.register(StudentProfile,StdProfile)
