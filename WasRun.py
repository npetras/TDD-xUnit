from TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        self.wasSetup = None
        self.wasRun = None
        TestCase.__init__(self, name)

    def setUp(self):
        self.wasRun = None
        self.wasSetup = 1

    def run(self):
        method = getattr(self, self.name)
        method()

    def testMethod(self):
        self.wasRun = 1
        pass
