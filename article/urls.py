from django.conf.urls import url

urlpatterns = [
	url(r'^1/', 'article.views.basic_one'),
	url(r'^2/', 'article.views.template_two'),
]
