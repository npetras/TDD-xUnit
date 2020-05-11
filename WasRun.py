from TestCase import TestCase


class WasRun(TestCase):
    def __init__(self, name):
        self.log = ""
        TestCase.__init__(self, name)

    def setUp(self):
        self.wasRun = None
        self.log = "setUp "

    def run(self):
        method = getattr(self, self.name)
        method()

    def testMethod(self):
        self.log = self.log + "testMethod "
        pass
