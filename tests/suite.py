import unittest
from mock import MagicMock

from seismograph.suite import MountData


class MountDataTest(unittest.TestCase):
    def setUp(self):
        self.config = MagicMock()
        self.mountDataObject = MountData(self.config)

    def testGetConfig(self):
        self.assertEqual(self.mountDataObject.config, self.config)
