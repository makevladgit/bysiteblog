# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Article(models.Model):
	class Meta():
		db_table = "article" 
		
	article_login = models.CharField(max_length = 200,verbose_name="Ваш логин")
	article_pass = 	models.CharField(max_length = 200,verbose_name="Ваш пароль")
