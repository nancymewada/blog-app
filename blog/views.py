# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render, get_object_or_404
import datetime as dt
from .forms import PostForm
from django.views.generic import View

def post_list(request):
	my_posts = Post.objects.all()
	context = []
	for i in my_posts:
		cntext = {}
		cntext['title'] = i.title
		cntext['auther'] = i.author.username
		cntext['text'] = i.text
		cntext['created'] = i.created_date.strftime('%Y-%m-%d %H:%M:%S')
		cntext['pk'] = i.pk
		context.append(cntext)
		i.publish()
	return render(request, 'blog/post_list.html', {'posts':context})


def post_detail(request):
	post = get_object_or_404(Post, pk=pk)
	return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_new1(request):

    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

