from django.shortcuts import render, get_object_or_404
from blog.models import Post


def index(request):
	posts = Post.objects.filter(published=True)
	data = {'posts': posts}
	return render(request, 'blog/index.html', data)


def post(request, slug):
	post = get_object_or_404(Post, slug=slug)
	data = {'post': post}
	return render(request, 'blog/post.html', data)
