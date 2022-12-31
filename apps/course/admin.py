from django.contrib import admin
from apps.course.models import *
from django.utils.html import format_html


# Register your models here.

#@admin.register(Course)
#class CurseAdmin(admin.ModelAdmin):
    #list_display = ("name",)
    #search_fields = ("name",)
class CourseUnitAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(Course, CourseUnitAdmin)
admin.site.register(Cohort)

