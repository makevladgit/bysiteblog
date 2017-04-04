from django.conf.urls import  url
from django.contrib import admin
from konkurs.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	#url(r'^basicview/1/$', basic_one),
	#url(r'^basicview/2/$', template_two),
	#url(r'^basicview/3/$', template_three_simple),
	#url(r'^articles/get/(?P<article_id>[0-9])/$', article),
	url(r'^$', index),
	url(r'^login/$', logingo),
	url(r'^loginl/$', login),
	url(r'^allpep/$', allpep),
	url(r'^nice/$', nicee),
	#url(r'^articles/addcomment/(?P<article_id>[0-9])/$', addcomment),
]
