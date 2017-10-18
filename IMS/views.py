from django.shortcuts import render, redirect, Http404, HttpResponse
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import permission_required
from .models import staff,Gstudent,Ustudent,blog,papers,indexContent
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.

def peoplePage(request):
    _staff=staff.objects.all()
    _Gstudent=Gstudent.objects.all()
    _Ustudent=Ustudent.objects.all()
    return render(request,'people.html',{'staff':_staff,'Gstudent':_Gstudent,'Ustudent':_Ustudent})

def indexPage(request):
    return render(request,'index.html')

def staffDetailPage(request,name):
    _staff=staff.objects.get(name=name)
    return render(request,'staffDetail.html',{'staff':_staff})

def GstudentDetailPage(request,name):
    _Gstudent=Gstudent.objects.get(name=name)
    return render(request,'staffDetail.html',{'staff':_Gstudent})

def UstudentDetailPage(request,name):
    _Ustudent=Ustudent.objects.get(name=name)
    return render(request,'staffDetail.html',{'staff':_Ustudent})

def blogHome(request):
    posts = blog.objects.all()
    paginator = Paginator(posts, 5)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return render(request, 'blog.html', {'post_list': post_list})

def blogDetail(request, id):
    try:
        post = blog.objects.get(id=str(id))
    except blog.DoesNotExist:
        raise Http404
    return render(request, 'blogDetail.html', {'post': post,'title':post.title})

def blogTag(request, tag):
    try:
        post_list = blog.objects.filter(category__iexact=tag)  # contains
    except blog.DoesNotExist:
        raise Http404
    return render(request, 'blogTag.html', {'post_list': post_list})


def blogSearch(request):
    if 'search' in request.GET:
        search_form = request.GET['search']
        if not search_form:
            return render(request, 'blog.html')
        else:
            post_list = blog.objects.filter(title__icontains=search_form)
            if len(post_list) == 0:
                return render(request, 'blog.html', {'post_list': post_list,'error': True})
            else:
                return render(request, 'blog.html', {'post_list': post_list,'error': False})
    return redirect('/blog/')