# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

import datetime

# Create your models here.

class CommentManager(models.Manager):

	def creator(self, postData):

		newComment = Comment.objects.create(text = postData['text'])

		return newComment


	def validator(self, postData):

		results = {
			'status': True,
			'errors': []
		}

		if postData['text'].isspace() == True:
			results['status'] = False,
			results['errors'].append('Comment cannot be all spaces')

		if len(postData['text']) < 3:
			results['status'] = False,
			results['errors'].append('Comment must be at least 3 characters')

		return results




class Comment(models.Model):
	text = models.CharField(max_length = 1000)
	created_at = models.DateTimeField(auto_now_add = True)
	objects = CommentManager()