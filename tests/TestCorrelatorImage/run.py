from pysys.constants import *
from pysys.basetest import BaseTest
from apama.correlator import CorrelatorHelper


class PySysTest(BaseTest):
	def execute(self):
		correlator = CorrelatorHelper(self)
		correlator.start(logfile='correlator.log', arguments=['--config', self.input+'/test.yaml'])
		correlator.flush()

	def validate(self):
		self.assertGrep('correlator.log', expr='Initialized python interpreter')
		self.assertGrep('correlator.log', expr='Correlator,.*running')
		self.assertGrep('correlator.log', expr='Java virtual machine created')
		self.assertGrep('correlator.log', expr='Hello World')

		self.assertGrep('correlator.log', expr='Loading Java class com.softwareag.connectivity.testplugins.UnitTestHarness for plug-in unitTestHarness')
		self.assertGrep('correlator.log', expr='Connectivity plug-ins: Loaded C.. plugin from path libconnectivity-http-server.so')
		self.assertGrep('correlator.log', expr='Connectivity plug-ins: Loaded C.. plugin from path libMapperCodec.so')
		self.assertGrep('correlator.log', expr='Connectivity plug-ins: Loaded C.. plugin from path libClassifierCodec.so')
		self.assertGrep('correlator.log', expr='Connectivity plug-ins: Loaded C.. plugin from path libconnectivity-json-codec.so')
		self.assertGrep('correlator.log', expr='Connectivity plug-ins: Loaded C.. plugin from path libconnectivity-string-codec.so')
		self.assertGrep('correlator.log', expr='Connectivity plug-ins: Loaded C.. plugin from path libDiagnosticCodec.so')
		self.assertGrep('correlator.log', expr='Connectivity plug-ins: Loaded C.. plugin from path libconnectivity-http-client.so')
		self.assertGrep('correlator.log', expr='Connectivity chain created, subscribed to no channels')
		self.assertGrep('correlator.log', expr='Connectivity chain created, subscribed to .http.')
		self.assertGrep('correlator.log', expr='Plugin library ManagementPlugin .* loaded OK')
		self.assertGrep('correlator.log', expr='Plugin library JSONPlugin .* loaded OK')
		self.assertGrep('correlator.log', expr='Plugin library TimeFormatPlugin .* loaded OK')
		self.assertGrep('correlator.log', expr='Plugin library MemoryStorePlugin .* loaded OK')

		self.assertGrep('correlator.log', expr='ERROR', contains=False)

