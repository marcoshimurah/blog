from django.db import models


class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(max_length=1000)
	date = models.DateTimeField(auto_now=True)

	
class Comment(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(max_length=1000)
	date = models.DateTimeField(auto_now=True)
	post = models.ForeignKey(Post)

	def __unicode__(self):
		return self.title	

