from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, Http404
from blogApp.models import CategoryModel, PostModel


def post_list_view(request: HttpRequest) -> HttpResponse:
    ctx = {
        'object_list': PostModel.objects.all(),
        'category_list': CategoryModel.objects.all(),
    }
    return render(request, 'homepage.html', ctx)


def post_detail_view(request: HttpRequest, slug: str) -> HttpResponse:
    try:
        post = PostModel.objects.get(slug=slug)
    except PostModel.DoesNotExist:
        raise Http404("Not found")
    ctx = {
        'object': post,
        'category_list': CategoryModel.objects.all(),
    }
    return render(request, 'post.html', ctx)
