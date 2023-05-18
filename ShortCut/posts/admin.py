from django.contrib import admin
from import_export.admin import ExportActionMixin
from .models import Post, Group, Comment, Follow


class PostAdmin(ExportActionMixin, admin.ModelAdmin):
    list_display = (
        'pk',
        'title',
        'pub_date',
        'author',
        'group'
    )
    list_editable = ('group',)
    search_fields = ('title',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(Post, PostAdmin)
admin.site.register(Group)
admin.site.register(Comment)
admin.site.register(Follow)
