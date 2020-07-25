from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

from django.contrib.auth.models import User
from users.models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    
    list_display = ('pk', 'user', 'phone_number', 'website')
    list_display_links = ('pk','user', 'phone_number')
    list_editable = ('website',) 

    list_filter = ('created', 'user__is_active')

    fieldsets = (
        ('profile', {
            'fields': (('user', 'picture'),),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', {
            'fields': (('created', 'modified'),),
        })
    )

    readonly_fields = ('created', 'modified', 'user')

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

    list_display = ('username', 'first_name', 'last_name')

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
