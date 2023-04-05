from django.contrib import admin
from .models import User
from django.utils.html import format_html

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    def get_pfp(self, obj):
        return format_html('<img src="{}" style="width:50px;height:50px"/>'.format(obj.pfp.url))
    get_pfp.allow_tags = True
    get_pfp.short_description = 'PFP'
    list_display = ('get_pfp','username', 'skills')

admin.site.register(User, UserAdmin)