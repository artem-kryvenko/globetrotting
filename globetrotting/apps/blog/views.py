from django.shortcuts import render
from blog.models import Post


def home(request):
	posts = Post.objects.filter(published=True)
	data = {'posts': posts}
	return render(request, 'blog/home.html', data)


def post_detail(request, post_id):
	post = Post.objects.get(id=post_id)
	post_photos = post.photo_set.all()
	data = {
		'post': post,
		'post_photos': post_photos,
	}
	return render(request, 'blog/post_detail.html', data)



def archive(request):
	posts = Post.objects.filter(published=True)
	data = {'posts': posts}
	return render(request, 'blog/archive.html', data)
