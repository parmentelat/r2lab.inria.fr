"""R2lab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^news/', include('news.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

import md.views
import mfauth.views
import leases.views
import slices.views
import users.views
import files.views
import keys.views

urlpatterns = [
    # default: empty or just / -> md/index.md
    url(r'^(/)?$', RedirectView.as_view(url='/index.md', permanent=False)),
    # no subdir
    url(r'^(?P<markdown_file>[^/]*)$', md.views.markdown_page),
    url(r'^md/(?P<markdown_file>.*)$', md.views.markdown_page),
    url(r'^login/', mfauth.views.Login.as_view()),
    url(r'^logout/', mfauth.views.Logout.as_view()),
    url(r'^leases/(?P<verb>(add|update|delete))', leases.views.LeasesProxy.as_view()),
    url(r'^slices/(?P<verb>(get|renew))', slices.views.SlicesProxy.as_view()),
    url(r'^users/(?P<verb>(get|renew))', users.views.UsersProxy.as_view()),
    url(r'^files/(?P<verb>(get))', files.views.FilesProxy.as_view()),
    url(r'^keys/(?P<verb>(get|add|delete))', keys.views.KeysProxy.as_view()),
    # probably not useful
#    url(r'^admin/', admin.site.urls),
] \
    + static( '/assets/', document_root=settings.BASE_DIR+'/assets/') \
    + static( '/raw/', document_root=settings.BASE_DIR+'/raw/') \
    + static( '/files/nodes/images/', document_root=settings.BASE_DIR+'/files/nodes/images/') \
    + static( '/files/nodes/images_dt/', document_root=settings.BASE_DIR+'/files/nodes/images_dt/') \
    + static( '/code/', document_root=settings.BASE_DIR+'/code/') 
