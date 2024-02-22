from django.contrib import admin
from .models import *


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ('name',)
    list_display_links = ('name',)
    ordering = ['name']
    list_per_page = 10
    search_fields = ['name']
    save_on_top = True

    class Meta:
        model = City


@admin.register(Street)
class StreetAdmin(admin.ModelAdmin):
    fields = ['name', 'city']
    list_display = ('name', 'city',)
    list_display_links = ('name', 'city',)
    ordering = ['name', 'city']
    list_per_page = 10
    search_fields = ['name']
    save_on_top = True

    class Meta:
        model = Street


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    fields = ['street', 'number', 'corpus']
    search_fields = ['street', 'number']
    ordering = ['street', 'number']
    list_per_page = 10
    save_on_top = True

    class Meta:
        model = Building


class WorkDayInline(admin.TabularInline):
    model = WorkDay
    extra = 0
    max_num = 7
    verbose_name = 'День недели'
    verbose_name_plural = 'Дни недели'

    def get_formset(self, request, obj=None, **kwargs):
        if obj and obj.name:
            self.max_num = 0  # Если поле name заполнено, не отображаем поля для добавления новых дней недели
        else:
            self.max_num = 7  # Если поле name не заполнено, отображаем все 7 дней недели
        return super().get_formset(request, obj, **kwargs)


@admin.register(WorkSchedule)
class WorkScheduleAdmin(admin.ModelAdmin):
    inlines = [WorkDayInline]
    # fields = ['user', 'title', 'slug', 'content']
    # list_display = ('title', 'created_at', 'updated_at')
    # list_display_links = ('title',)
    # ordering = ['created_at', 'title']
    # list_per_page = 10
    # search_fields = ['title']
    # save_on_top = True
    # prepopulated_fields = {'slug': ('title',)}

    # def get_formset(self, request, obj=None, **kwargs):
    #     if obj and obj.name:
    #         self.inlines = [WorkDayInline]
    #     else:
    #         self.inlines = []
    #     return super().get_formset(request, obj, **kwargs)

    class Meta:
        model = WorkSchedule





