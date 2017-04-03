from django.forms import ModelForm
from article.models import Comments

class CommentForm(ModelForm):
 class Meta:
  model = Comments
  fields = ['comments_text']