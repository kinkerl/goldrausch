from django.core.management.base import BaseCommand, CommandError
import os
import subprocess
from django.conf import settings
import sys

#generate the doc
class Command(BaseCommand):
	args = ''
	help = 'compress'

	def handle(self, *args, **options):
		ALLOWED_TARGETS = ['media', 'static']
		
		
		if len(args)<= 0 or not args[0] in ALLOWED_TARGETS:
                        print "compress target not specified, please select: %s" % ", ".join(ALLOWED_TARGETS)
                        sys.exit(1)
		else:
	                TARGET = args[0]

		try:
			if TARGET == 'media':
				TARGET_ROOT = settings.MEDIA_ROOT
			elif TARGET == 'static':
				TARGET_ROOT = settings.STATIC_ROOT
			else:
				TARGET_ROOT = False
		except AttributeError: #happens when settings.ELITIST_GRAPH_MODELS_LIST does not exist
			TARGET_ROOT = False

		if TARGET_ROOT:
			callcmd = []#trimage -v -d
			callcmd.append('trimage')
			callcmd.append('-q')
			#callcmd.append('-v')
			callcmd.append('-d')
			callcmd.append(TARGET_ROOT)
			p = subprocess.call(callcmd, close_fds=True, env=os.environ )
		else:
			print "MEDIA_ROOT not set"
