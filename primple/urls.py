"""primple URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, include
from django.contrib import admin
from knowledge_base import views as knowledge_base_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    
    #Authenticate
 	url(r'^accounts/login/$', knowledge_base_views.login),
	url(r'^accounts/auth/$', knowledge_base_views.auth_view),
	url(r'^accounts/logout/$', knowledge_base_views.logout),
	url(r'^accounts/loggedin/$', knowledge_base_views.loggedin),
	url(r'^accounts/invalid/$', knowledge_base_views.invalid_login),
	url(r'^accounts/register/$', knowledge_base_views.register_user),
	url(r'^accounts/register_success/$', knowledge_base_views.register_success),

    # user_desktop
    url(r'^user_desktop/', knowledge_base_views.user_desktop),

    # knowledge_base
    #url(r'^knowledge_base/$', knowledge_base_views.getList, name='getList')
    url(r'^knowledge_base/$', knowledge_base_views.index),
    url(r'^knowledge_base/get/(?P<knowledge_base_id>\d+)/$', knowledge_base_views.knowledge_base_entry),
    url(r'^knowledge_base/new/$', knowledge_base_views.knowledge_base_new),
    url(r'^$', knowledge_base_views.home)
]
