from pysys.constants import *
from pysys.basetest import BaseTest
from apama.correlator import CorrelatorHelper

class PySysTest(BaseTest):
	def execute(self):
		correlator = CorrelatorHelper(self)
		correlator.start(logfile='correlator.log', arguments=['--config', self.input+'/project'])
		correlator.injectJava('test.jar')
		correlator.injectEPL('test.mon')
		correlator.flush()

	def validate(self):
		self.assertGrep('correlator.log', expr='test ... Loaded monitor test')
		self.assertGrep('correlator.log', expr='Injected JMon application TestPluginApplication')
		self.assertGrep('correlator.log', expr='m ... Hello World')

		self.assertGrep('correlator.log', expr='ERROR', contains=False)

