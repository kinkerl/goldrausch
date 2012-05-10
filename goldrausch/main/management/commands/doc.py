from django.core.management.base import BaseCommand, CommandError
import os
import subprocess
from django.conf import settings


#generate the doc
class Command(BaseCommand):
	args = ''
	help = 'generate the documentation'

	def handle(self, *args, **options):

		try:
			ELITIST_GRAPH_MODELS_LIST = settings.ELITIST_GRAPH_MODELS_LIST
		except AttributeError: #happens when settings.ELITIST_GRAPH_MODELS_LIST does not exist
			ELITIST_GRAPH_MODELS_LIST = []

		if ELITIST_GRAPH_MODELS_LIST:
			for element in settings.ELITIST_GRAPH_MODELS_LIST:
				self.stdout.write("generating image: %s\n" % element)
				os.popen("./manage.py graph_models %s |dot -Tpng -o ../doc/images/%s.png" % (element, element))
		else:
			print "no app selected for creating graph models, see ELITIST_GRAPH_MODELS_LIST"

		callcmd = []
		callcmd.append('make')
		callcmd.append('html')
		p = subprocess.call(callcmd, close_fds=True, env=os.environ, cwd="../doc" )
		#os.popen("cd ../doc/ && make html")
