from django.forms import ModelForm
from konkurs.models import Article

class CommentForm(ModelForm):
	class Meta:
		model = Article
		fields = ['article_login','article_pass']