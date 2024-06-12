from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from kafedra.models import Kafedra


def kafedra_home(request):
    posts = Kafedra.objects.all()
    return render(request, 'kafedra/index.html', {'posts': posts})


def show_kafedra(request, post_slug):
    post = get_object_or_404(Kafedra, slug=post_slug)
    return render(request, 'kafedra/post.html', {'post': post})




