from django.shortcuts import render
from main.models import Bookmark
from django.http import  JsonResponse
from .models import Todo

from django.http import HttpResponseRedirect
from django.urls import reverse

from accounts.models import User

from django.db.models import Q


def details(request):
    return render(request, 'mypage.html')


def bookmark(request):
    bookmark_all = Bookmark.objects.order_by('-pk')
    bookmarks=bookmark_all.filter(user_id=request.session['user_id'])
    context = {
        'bookmarks': bookmarks
    }
    return render(request, 'bookmark.html', context)

def index(request):
    todo_all = Todo.objects.all()
    todo_items=todo_all.filter(user_id=request.session['user_id'])
    return render(request,'todo.html',{'todo_items':todo_items})

def create(request):
    item = Todo.objects.create(title = request.POST['title'], user_id=request.session['user_id'])
    return JsonResponse({
        'id': item.id,
        'title': item.title,
        'completed': item.completed
    }, status=200)

def mark_complete(request):
    if request.is_ajax and request.method == "POST":
        item = Todo.objects.filter(id=request.POST['id']).update(completed=True)
        return JsonResponse({"success": "true"}, status=200)
    # some error occured
    return JsonResponse({"error": ""}, status=400)

def mark_uncomplete(request):
    if request.is_ajax and request.method == "POST":
        item = Todo.objects.filter(id=request.POST['id']).update(completed=False)
        return JsonResponse({"success": "true"}, status=200)
    return JsonResponse({"error": ""}, status=400)

def delete(request):
    if request.is_ajax and request.method == "POST":
        item = Todo.objects.filter(id=request.POST['id']).delete()
        return JsonResponse({"success": "true"}, status=200)
    return JsonResponse({"error": ""}, status=400)

def search(request):
    bookmark_all = Bookmark.objects.order_by('-pk')
    search_keyword = request.GET.get('title')
    bookmarks = bookmark_all.filter(
        Q(content__icontains=search_keyword), user_id=request.session['user_id'])
    context = {
        'bookmarks': bookmarks
    }
    return render(request, 'bookmark.html', context)
