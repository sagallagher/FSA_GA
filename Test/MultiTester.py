from Test.Tester import *
from Test.ConfigParser import *
import sys
import os, os.path
class MultiTester():

    def __init__(self,cp):
        self.cp = cp


    def generateOneOutput(self):

        for filename in os.listdir(self.cp.getSetting('DIRECTORY')):
            os.remove(os.path.join(self.cp.getSetting('DIRECTORY'),filename))
        t = Tester(self.cp)

        t.run()

    def incrementConfigFile(self):
        pass

    # generate (ALPHABET_SIZE-min) * (EXAMPLES_PER_FILE-min) outputs
    def generateMultOutput(self, output_dir):

        filenum = 0
        for i in range(int(self.cp.getSetting("MIN_ALPHABET_SIZE")),
            int(self.cp.getSetting('MAX_ALPHABET_SIZE'))+1):

            self.cp.settings['MAX_ALPHABET_SIZE'] = i

            for j in range(int(self.cp.getSetting("MIN_EXAMPLES_PER_FILE")),
                int(self.cp.getSetting("MAX_EXAMPLES_PER_FILE"))+1):

                self.cp.settings['FILE_PREFIX'] = str(filenum)
                self.cp.settings['OUTPUT_FILE'] = os.path.join(output_dir,str(filenum))
                self.cp.settings['EXAMPLES_PER_FILE'] = j
                filenum+=1
                self.generateOneOutput()
