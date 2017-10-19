"""imsPJ URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
import IMS.views as IMSview
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IMSview.indexPage, name='index'),
    url(r'^people/$', IMSview.peoplePage, name='people'),
    url(r'^people/(?P<name>\w+)/$', IMSview.staffDetailPage, name='staffDetail'),
    url(r'^blog/$', IMSview.blogHome, name='blog'),
    url(r'^blog/detail/(?P<id>\d+)$', IMSview.blogDetail, name='blogDetail'),
    url(r'^blog/tag/(?P<tag>\w+)/$', IMSview.blogTag, name='blogTag'),
    url(r'^blog/search/$', IMSview.blogSearch, name='blogSearch'),
    url(r'^publication/$', IMSview.publicationHome, name='publication'),
    url(r'^publication/tag/(?P<tag>\w+)/$', IMSview.publicationTag, name='publicationTag'),
    url(r'^publication/year/(?P<year>\w+)/$', IMSview.publicationYear, name='publicationYear'),
    url(r'^publication/search/$', IMSview.publicationSearch, name='publicatinoSearch'),

]
# Use static file server for static and media files (debug only)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)