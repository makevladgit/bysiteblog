from django.conf.urls import  url
from django.contrib import admin
from article.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^basicview/1/$', basic_one),
	url(r'^basicview/2/$', template_two),
	url(r'^basicview/3/$', template_three_simple),
	url(r'^articles/get/(?P<article_id>[0-9])/$', article),
	url(r'^$', articles),
	url(r'^articles/addlike/(?P<article_id>[0-9])/$', addlike),
	url(r'^articles/addcomment/(?P<article_id>[0-9])/$', addcomment),
]
