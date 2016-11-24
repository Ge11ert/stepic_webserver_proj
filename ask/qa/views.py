from django.shortcuts import render
from django.http import HttpResponse, HttpRequest, QueryDict, Http404
from django.core.paginator import Paginator, EmptyPage
from qa.models import Question, Answer
from __builtin__ import int
# Create your views here.

def test(request, *args, **kwargs):
    return HttpResponse('test_string')

def pop_test(request, *args, **kwargs):
    
    return HttpResponse('<h1> This is popular-questions page! </h1>')

def new_test(request, *args, **kwargs):
    return HttpResponse('<h1> This is new-questions page! </h1>')

def list_new(request):
    new_posts = Question.objects.new()
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
    return render(request, 'questionList.html', {
        'posts': page.object_list,
        'page': page,
        'paginator': paginator,
        })

def list_popular(request):
    popular_posts = Question.objects.popular()
    limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(popular_posts, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    paginator.baseurl = '/?page='
    return render(request, 'questionList.html', {
        'posts': page.object_list,
        'page': page,
        'paginator': paginator,
        })
    
def question(request, question_id):
    try:
        quest = Question.objects.get(id = question_id)
    except Question.DoesNotExist:
        raise Http404
    answers = Answer.objects.filter(question = quest)
    
    title = 'qwest ' + question_id
    
    return render(request, 'question.html', {
        'title': title,
        'question': quest,
        'posts': answers,
        })
