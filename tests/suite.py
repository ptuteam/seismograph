import unittest
from mock import MagicMock

from seismograph.suite import MountData, SuiteContext


class MountDataTest(unittest.TestCase):
    def setUp(self):
        self.config = MagicMock()
        self.mountDataObject = MountData(self.config)

    def testGetConfig(self):
        self.assertEqual(self.mountDataObject.config, self.config)


class SuiteContextTest(unittest.TestCase):
    def setUp(self):
        self.setup = MagicMock()
        self.teardown = MagicMock()

        self.suiteContextEmptyObject = SuiteContext(self.setup, self.teardown)
        self.suiteContextObject = SuiteContext(self.setup, self.teardown)

    def testGetRequire(self):
        self.assertEqual(self.suiteContextEmptyObject.require, [])

    def testGetExtensions(self):
        self.assertEqual(self.suiteContextEmptyObject.extensions, {})

    def testGetBuildRules(self):
        self.assertEqual(self.suiteContextEmptyObject.build_rules, [])

    def testGetSetupCallbacks(self):
        self.assertEqual(self.suiteContextEmptyObject.setup_callbacks, [self.setup])

    def testGetTeardownCallbacks(self):
        self.assertEqual(self.suiteContextEmptyObject.teardown_callbacks, [self.teardown])

    def testGetLayers(self):
        for layer in self.suiteContextEmptyObject.layers:
            self.assertEqual(layer, None)

    def testAddLayers(self):
        self.suiteContextObject.add_layers([])
        for layer in self.suiteContextObject.layers:
            self.assertEqual(layer, None)

        layer1 = MagicMock()
        self.suiteContextObject.add_layers([layer1])
        self.assertEqual(self.suiteContextObject.layers.next(), layer1)

        layer2 = MagicMock()
        self.suiteContextObject.add_layers([layer2])
        layers = self.suiteContextObject.layers
        self.assertEqual(layers.next(), layer1)
        self.assertEqual(layers.next(), layer2)

        layer3 = MagicMock()
        layer4 = MagicMock()
        self.suiteContextObject.add_layers([layer3, layer4])
        layers = self.suiteContextObject.layers
        self.assertEqual(layers.next(), layer1)
        self.assertEqual(layers.next(), layer2)
        self.assertEqual(layers.next(), layer3)
        self.assertEqual(layers.next(), layer4)
