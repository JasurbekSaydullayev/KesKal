from django.contrib import admin

from debtors.models import Debtor


@admin.register(Debtor)
class DebtorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone_number', 'amount', 'vendor')
