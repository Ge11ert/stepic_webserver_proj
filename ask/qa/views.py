from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, QueryDict, Http404
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question
from __builtin__ import int
from django.http.response import HttpResponseNotFound
# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('test_string')

def pop_test(request, *args, **kwargs):
    
    return HttpResponse('<h1> This is popular-questions page! </h1>')

def new_test(request, *args, **kwargs):
    return HttpResponse('<h1> This is new-questions page! </h1>')

def list_new_posts(request):
    new_posts = Question.objects.new()
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(new_posts, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    paginator.baseurl = '/?page='
    return render(request, 'new_posts.html', {
        'new_posts': page.object_list,
        'page': page,
        'paginator': paginator,
        })


