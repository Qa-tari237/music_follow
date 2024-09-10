# myapp/admin.py

from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'user_id', 'user_email', 'profile_picture_display')

    def user_id(self, obj):
        return obj.user.id

    def user_email(self, obj):
        return obj.user.email

    def profile_picture_display(self, obj):
        if obj.profile_picture:
            return Profile('<img src="{}" style="width: 50px; height: 50px;" />', obj.profile_picture.url)
        return "-"

    profile_picture_display.short_description = 'Profile Picture'
    user_id.short_description = 'User ID'
    user_email.short_description = 'Email'

admin.site.register(Profile, ProfileAdmin)


# streaming
from django.contrib import admin
from .models import LiveSession, Subscriber, Reaction

admin.site.register(LiveSession)
admin.site.register(Subscriber)
admin.site.register(Reaction)