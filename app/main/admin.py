from django.contrib import admin

from main.models import *

class CountryLocalAdmin(admin.TabularInline):
    model = CountryLocal
    extra = 0

class CountryAdmin(admin.ModelAdmin):
    model = Country
    inlines = [CountryLocalAdmin,]
    search_fields = list_display = ['code', 'name']


class DomainLocalAdmin(admin.TabularInline):
    model = DomainLocal
    extra = 0

class DomainAdmin(admin.ModelAdmin):
    model = Domain
    inlines = [DomainLocalAdmin,]
    search_fields = list_display = ['name']


class ProfileLocalAdmin(admin.TabularInline):
    model = ProfileLocal
    extra = 0

class ProfileAdmin(admin.ModelAdmin):
    model = Profile
    inlines = [ProfileLocalAdmin,]


class IndicatorLocalAdmin(admin.TabularInline):
    model = IndicatorLocal
    extra = 0

class IndicatorAdmin(admin.ModelAdmin):
    model = Indicator
    inlines = [IndicatorLocalAdmin,]
    search_fields = list_display = ['code', 'name']
    ordering = ('code',)

class CountryIndicatorData(admin.TabularInline):
    model = CountryIndicatorData
    extra = 0


class CountryIndicatorAdmin(admin.ModelAdmin):
    model = CountryIndicator
    inlines = [CountryIndicatorData,]


admin.site.register(Country, CountryAdmin)
admin.site.register(Domain, DomainAdmin)
admin.site.register(Indicator, IndicatorAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(CountryIndicator, CountryIndicatorAdmin)


