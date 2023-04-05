from django.contrib import admin
from .models import Job
# Register your models here.


class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'skills', 'price', 'posted')

    # def get_applied(self, obj):
    #     return ', '.join(applied.name for applied in obj.applied.all())


admin.site.register(Job, JobAdmin)

