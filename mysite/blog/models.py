from django.db import models
from django.utils import timezone
from operator import attrgetter


class Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text= models.TextField()
	created_date = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True, auto_now=True)
	
	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title


class Estado(models.Model):
	estado = models.CharField(max_length=50)
	sigla = models.CharField(max_length=2)

	