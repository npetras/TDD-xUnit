from TestCase import TestCase
from WasRun import WasRun


class TestCaseTest(TestCase):
    def testSetUp(self):
        test = WasRun("testMethod")
        test.run()
        assert test.wasSetup

    def testRunning(self):
        test = WasRun("testMethod")
        test.run()
        assert test.wasRun
