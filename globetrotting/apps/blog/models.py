# -*- coding:utf-8 -*-

from django.db import models
from django.contrib import admin

from PIL import Image
import os


def _add_thumb(s):
	parts = s.split(".")
	parts.insert(-1, "thumb")
	if parts[-1].lower() not in ['jpeg', 'jpg']:
		parts[-1] = 'jpg'
	return ".".join(parts)


def _del_thumb(p):
	thumb_path = _add_thumb(p)
	if os.path.exists(thumb_path):
		os.remove(thumb_path)


class Post(models.Model):
	title = models.CharField(max_length=255)
	slug = models.SlugField(unique=True, max_length=255)
	description = models.CharField(max_length=255)
	content = models.TextField()
	created = models.DateField(auto_now_add=True)
	published = models.BooleanField(default=True)

	class Meta:
		ordering = ['-created']

	def __unicode__(self):
		return self.title


class Photo(models.Model):
	post = models.ForeignKey(Post)
	image = models.ImageField(upload_to='gallery')
	title = models.CharField(max_length=100, blank=True)
	caption = models.CharField(max_length=100, blank=True)

	class Meta:
		ordering = ['-id']
		# verbose_name = ('Photo')
		# verbose_name_plural = ('Photos')

	def __unicode__(self):
		return self.title

	def _get_thumb_path(self):
		return _add_thumb(self.image.path)
	thumb_path = property(_get_thumb_path)

	def _get_thumb_url(self):
		return _add_thumb(self.image.url)
	thumb_url = property(_get_thumb_url)

	def get_thumb_html(self):
		html = "<a class='image-picker' href='%s'><img src='%s' alt='%s'/></a>"
		return html % (self.image.url, _add_thumb(self.image.url), self.caption)
	thumb_html = property(get_thumb_html)
	get_thumb_html.short_description = ('Photo')
	get_thumb_html.allow_tags = True

	def save(self, force_insert=False, force_update=False):
		try:
			obj = Photo.objects.get(id=self.id)
			if obj.image.path != self.image.path:
				_del_thumb(obj.image.path)
				obj.image.delete()
		except:
			pass
		super(Photo, self).save()
		img = Image.open(self.image.path)
		img.thumbnail(
			(128, 128),
			Image.ANTIALIAS
		)
		img.save(self.thumb_path, 'JPEG')

	def delete(self):
		try:
			obj = Photo.objects.get(id=self.id)
			_del_thumb(obj.image.path)
			obj.image.delete()
		except:
			pass
		super(Photo, self).delete()

	def get_absolute_url(self):
		return ('photo_detail', None, {'object_id': self.id})

















































