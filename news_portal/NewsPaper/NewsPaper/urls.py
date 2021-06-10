
from django.contrib import admin
from django.urls import path
from django.urls import include

#translate
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('news/', include('news.urls')),
    path('sign/', include('sign.urls')),
    path('', include('protect.urls')),
    path('accounts/', include('allauth.urls')),
    path('i18n/', include('django.conf.urls.i18n')),
]

#urlpatterns += i18n_patterns(
#    path('', include(''))
#)
