from django.contrib import admin
from .models import ConnectionRequest, StudentProfile,StudentTransaction,Coincheck,ConnectionRequest



class StdProfile(admin.ModelAdmin):
    list_display = ('user','fullname','wallet_amount','account_verified')
    list_display_links = ('fullname','user')
    list_filter = ('account_verified',)
    search_fields = ('wallet_amount','fullname','user')

    class Meta:
        model = StudentProfile

class CoincheckS(admin.ModelAdmin):
    list_display = ('name','coindate',)
    list_display_links = ('name','coindate')


class Transaction(admin.ModelAdmin):
    list_display = ('fullname','amount','created','paid')
    list_filter = ('paid',)

class ConnectionRequestAdmin(admin.ModelAdmin):
    list_filter = ('sender','receiver')
    list_display = ('sender','receiver')
    search_fields = ('sender__username','receiver__username','sender__email','receiver__email')

    class Meta:
        model = ConnectionRequest


admin.site.register(StudentTransaction,Transaction)
admin.site.register(Coincheck,CoincheckS)
admin.site.register(StudentProfile,StdProfile)
admin.site.register(ConnectionRequest,ConnectionRequestAdmin)
