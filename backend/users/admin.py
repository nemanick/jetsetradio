from django.contrib import admin
from .models import CustomUser, Subscribe, UserOptions


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'veritificated',)
    search_fields = ('username', 'email',)
    ordering = ('username',)


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Subscribe)
admin.site.register(UserOptions)
