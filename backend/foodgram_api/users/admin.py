from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    empty_value_display = 'значение отсутствует'
    list_filter = ('email', 'username')


admin.site.register(User)
