from django.contrib import admin
from .models import Member


class MemberAdmin(admin.ModelAdmin):
    list_display = ('Name', 'Skills', 'Phone')
    search_fields = ('Name', 'Skills')


admin.site.register(Member, MemberAdmin)
