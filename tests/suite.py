import unittest
from mock import MagicMock

from seismograph.suite import MountData, BuildRule


class MountDataTest(unittest.TestCase):
    def setUp(self):
        self.config = MagicMock()
        self.mountDataObject = MountData(self.config)
        self.mountNoneDataObject = MountData()

    def testGetConfig(self):
        self.assertEqual(self.mountDataObject.config, self.config)

    def testGetNoneConfig(self):
        self.assertEqual(self.mountNoneDataObject.config, None)


class BuildRuleTest(unittest.TestCase):
    def setUp(self):
        self.suiteName = "suite"
        self.caseName = "case"
        self.testName = "test"

        self.buildRuleObject1 = BuildRule(self.suiteName)
        self.buildRuleObject2 = BuildRule(self.suiteName, self.caseName)
        self.buildRuleObject3 = BuildRule(self.suiteName, self.caseName, self.testName)

        self.suite = MagicMock()
        self.suite.name = self.suiteName

    def testGetSuiteName(self):
        self.assertEqual(self.buildRuleObject1.suite_name, self.suiteName)
        self.assertEqual(self.buildRuleObject2.suite_name, self.suiteName)
        self.assertEqual(self.buildRuleObject3.suite_name, self.suiteName)

    def testGetCaseName(self):
        self.assertEqual(self.buildRuleObject1.case_name, None)
        self.assertEqual(self.buildRuleObject2.case_name, self.caseName)
        self.assertEqual(self.buildRuleObject3.case_name, self.caseName)

    def testGetTestName(self):
        self.assertEqual(self.buildRuleObject1.test_name, None)
        self.assertEqual(self.buildRuleObject2.test_name, None)
        self.assertEqual(self.buildRuleObject3.test_name, self.testName)

    def testIsOf(self):
        self.assertEqual(self.buildRuleObject1.is_of(self.suite), True)
        self.assertEqual(self.buildRuleObject1.is_of(MagicMock()), False)

    def testGetObjectStr(self):
        self.assertEqual(str(self.buildRuleObject1), self.suiteName)
        self.assertEqual(str(self.buildRuleObject2), self.suiteName + ':' + self.caseName)
        self.assertEqual(str(self.buildRuleObject3), self.suiteName + ':' + self.caseName + '.' + self.caseName)

    def testGetObjectRepr(self):
        self.assertEqual(
            repr(self.buildRuleObject1),
            '<{}(suite_name={}, case_name={}, test_name={})>'.format(
                self.buildRuleObject1.__class__.__name__,
                self.suiteName,
                None,
                None
            )
        )
        self.assertEqual(
            repr(self.buildRuleObject2),
            '<{}(suite_name={}, case_name={}, test_name={})>'.format(
                self.buildRuleObject2.__class__.__name__,
                self.suiteName,
                self.caseName,
                None
            )
        )
        self.assertEqual(
            repr(self.buildRuleObject3),
            '<{}(suite_name={}, case_name={}, test_name={})>'.format(
                self.buildRuleObject3.__class__.__name__,
                self.suiteName,
                self.caseName,
                self.testName
            )
        )
