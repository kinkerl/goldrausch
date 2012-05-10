from django.core.management.base import BaseCommand, CommandError
import os
import subprocess
from django.conf import settings
import sys

#generate the doc
class Command(BaseCommand):
	args = ''
	help = 'generate the documentation'

	def handle(self, *args, **options):

		TARGET = args[0]
		if not TARGET:
			print "no target specified"
			sys.exit(1)

		try:
			ELITIST_RELEASE_TARGET = settings.ELITIST_RELEASE_TARGET
		except AttributeError: #happens when settings.ELITIST_GRAPH_MODELS_LIST does not exist
			ELITIST_RELEASE_TARGET = []

		# rsync -r -e ssh ../out/*  staging:/home/web/mb/fashion.mb.sv-preview.de/site/htdocs/test
		if TARGET in ELITIST_RELEASE_TARGET:
			print "pushing to %s" % TARGET
			
			callcmd = []
			callcmd.append('rsync')
			callcmd.append('-r')
			callcmd.append('-e')
			callcmd.append('ssh')
			callcmd.append('../out/')
			callcmd.append("%s:%s" % ELITIST_RELEASE_TARGET[TARGET])
			print " ".join(callcmd)
			p = subprocess.call(callcmd, close_fds=True, env=os.environ)
		else:
			print "target unknown"
		#os.popen("cd ../doc/ && make html")
