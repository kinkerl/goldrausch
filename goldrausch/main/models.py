# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.conf import settings


class Agent(models.Model):
	"""
	Ein Device von dem Anfragen erwartet werden
	"""
	name = models.CharField(max_length=50, help_text=_("Menschenlesbarer Name"))
	secret = models.CharField(max_length=50, help_text=_("Geheimer Schluessel der im Board hinterlegt werden muss"))
	code = models.IntegerField(help_text=_("Code mit dem sich ein Agent beim Server identifiziert"))

	def __unicode__(self):
		return "%d//%s" %(self.code,self.name)


class Task(models.Model):
	"""
	Ein Moeglicher Task der vom Client beobachtet wird
	"""
	aegnt = models.ForeignKey(Agent)
	name = models.CharField(max_length=50, help_text=_("Menschenlesbarer Name"))
	code = models.IntegerField(help_text=_("Code der diesen Task beschreibt"))
	status = models.IntegerField(default=0, help_text=_("Aktueller Status des Tasks"))

	def __unicode__(self):
		return "%d//%s" %(self.code,self.name)

