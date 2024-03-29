"""secretary2 URL Configuration

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
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from web import views
from django.contrib.auth import views as auth_views


urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^diary/(?P<month>\d+)/$', views.diary),
        url(r'^diary/add/$', views.diary_add),
        url(r'^diary/word/(?P<month>\d+)/$', views.diary_word),
        url(r'^home/$', views.home),
        url(r'^money/(?P<month>\d+)$', views.money),
        url(r'^money/add/$', views.money_add),
        url(r'^money/excel/(?P<month>\d+)/$', views.money_excel),
        url(r'^$', views.user_login),
        url(r'^logout/$',auth_views.logout),
        url(r'^pigbloodcake', 'show.views.pigbloodcake'),
        url(r'^alivetocopus', 'show.views.alivetocopus'),
        url(r'^grasshopper', 'show.views.grasshopper'),
        url(r'^pigeon', 'show.views.pigeon'),
        url(r'^durian/$', 'show.views.durian'),
        url(r'^login', views.user_login),
]