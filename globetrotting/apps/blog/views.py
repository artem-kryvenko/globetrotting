from django.shortcuts import render, get_object_or_404
from blog.models import Post


def home(request):
	posts = Post.objects.filter(published=True)
	data = {'posts': posts}
	return render(request, 'blog/home.html', data)


def post_detail(request, post_id):
	post = Post.objects.get(id=post_id)
	data = {'post': post}
	return render(request, 'blog/post_detail.html', data)


def archive(request):
	posts = Post.objects.filter(published=True)
	data = {'posts': posts}
	return render(request, 'blog/archive.html', data)
