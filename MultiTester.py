from Test.Tester import *
from Test.ConfigParser import *
import os, os.path
class MultiTester():

    def __init__(self,cp):
        self.cp = cp


    def generateOneOutput(self):
        t = Tester(self.cp)

        t.run()

    def generateMultOutput(self, output_dir, output_count):

        for i in range(output_count):
            self.cp.settings['FILE_PREFIX'] = i
            self.cp.settings['OUTPUT_FILE'] = os.path.join(output_dir,str(i))
            self.cp.settings['ALPHABET_SIZE'] = i+2
            self.generateOneOutput()


c = ConfigParser()
c.parse('config.txt')
m = MultiTester(c)



m.generateMultOutput('/home/me/scripts/python/AutoAutomata/FSA_GA/Data/output/tout',5)
