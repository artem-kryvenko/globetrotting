# -*- coding:utf-8 -*-
from django.contrib import admin
from blog.models import Post, Photo


class PhotoInline(admin.StackedInline):
	model = Photo


class PostAdmin(admin.ModelAdmin):
	list_display = ['title', 'description']
	list_filter = ['published', 'created']
	search_fields = ['title', 'description', 'content']
	date_hierarchy = 'created'
	save_on_top = True
	prepopulated_fields = {'slug': ('title',)}
	inlines = [PhotoInline]


class PhotoAdmin(admin.ModelAdmin):
	admin.site.disable_action('delete_selected')

	def full_delete_selected(self, request, obj):
		for o in obj.all():
			o.delete()
	full_delete_selected.short_description = 'Delete selected photos'
	actions = ['full_delete_selected']
	list_display = ('title', 'caption', 'get_thumb_html')


admin.site.register(Post, PostAdmin)
admin.site.register(Photo, PhotoAdmin)