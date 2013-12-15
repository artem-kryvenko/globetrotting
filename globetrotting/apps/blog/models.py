from django.db import models
from django.core.urlresolvers import reverse


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
		return "%s" % self.title

	def get_absolute_url(self):
		return reverse('blog.views.post', args=[self.slug])
