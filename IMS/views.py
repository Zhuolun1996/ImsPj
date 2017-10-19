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
    categories=posts.values('category').distinct().order_by('category')
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    try:
        postList = paginator.page(page)
    except PageNotAnInteger:
        postList = paginator.page(1)
    except EmptyPage:
        postList = paginator.page(paginator.num_pages)
    return render(request, 'blog.html', {'post_list': postList,'categories':categories})

def blogDetail(request, id):
    categories = blog.objects.all().values('category').distinct().order_by('category')
    try:
        post = blog.objects.get(id=str(id))
    except blog.DoesNotExist:
        raise Http404
    return render(request, 'blogDetail.html', {'post': post,'title':post.title,'categories':categories})

def blogTag(request, tag):
    categories = blog.objects.all().values('category').distinct().order_by('category')
    try:
        postList = blog.objects.filter(category__iexact=tag)  # contains
    except blog.DoesNotExist:
        raise Http404
    return render(request, 'blogTag.html', {'post_list': postList,'categories':categories})


def blogSearch(request):
    categories = blog.objects.all().values('category').distinct().order_by('category')
    if 'search' in request.GET:
        search_form = request.GET['search']
        if not search_form:
            return render(request, 'blog.html')
        else:
            postList = blog.objects.filter(title__icontains=search_form)
            return render(request, 'blog.html', {'post_list': postList,'categories':categories})
    return redirect('/blog/')

def publicationHome(request):
    paperList = papers.objects.all()
    categories = paperList.values('category').distinct().order_by('category')
    years = paperList.values('year').distinct().order_by('year')
    paginator = Paginator(paperList, 10)
    page = request.GET.get('page')
    try:
        postList = paginator.page(page)
    except PageNotAnInteger:
        postList = paginator.page(1)
    except EmptyPage:
        postList = paginator.page(paginator.num_pages)
    return render(request, 'publications.html', {'post_list': postList,'categories':categories,'years':years})

def publicationTag(request, tag):
    paperList=papers.objects.all()
    categories=paperList.values('category').distinct().order_by('category')
    years=paperList.values('year').distinct().order_by('year')
    try:
        paperList = papers.objects.filter(category__iexact=tag)  # contains
    except papers.DoesNotExist:
        raise Http404
    return render(request, 'publications.html', {'post_list': paperList,'categories':categories,'years':years})

def publicationYear(request, year):
    paperList=papers.objects.all()
    categories = paperList.values('category').distinct().order_by('category')
    years = paperList.values('year').distinct().order_by('year')
    try:
        paperList = papers.objects.filter(year__iexact=year)  # contains
    except papers.DoesNotExist:
        raise Http404
    return render(request, 'publications.html', {'post_list': paperList,'categories':categories,'years':years})

def publicationSearch(request):
    paperList = papers.objects.all()
    categories = paperList.values('category').distinct().order_by('category')
    years = paperList.values('year').distinct().order_by('year')
    if 'search' in request.GET:
        search_form = request.GET['search']
        if not search_form:
            return render(request, 'publications.html')
        else:
            paperList = papers.objects.filter(title__icontains=search_form)
            return render(request, 'publications.html', {'post_list': paperList,'categories':categories,'years':years})
    return redirect('/publication/')

