from django.contrib import admin
from .models import Memo


@admin.register(Memo)
class MemoAdmin(admin.ModelAdmin):
	list_display = ('title', 'author', 'created_at')
	search_fields = ('title', 'content')

