from django.contrib import admin

from market.models import Market, Statistics


@admin.register(Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


@admin.register(Statistics)
class StatisticsAdmin(admin.ModelAdmin):
    list_display = ('id', 'trade')
