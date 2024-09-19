import os

from django.contrib import admin, auth
from django.urls import include, path, re_path
from django.views.static import serve

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.join(BASE_DIR, 'site')

urlpatterns = [
    path('', include('home.urls')),
    path('cats/', include('cats.urls')),
    path('autos/', include('autos.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('hello/', include('hello.urls')),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    re_path(r'^site/(?P<path>.*)$', serve,
         {'document_root': SITE_ROOT, 'show_indexes': True},
         name='site_path'
    ),
]
