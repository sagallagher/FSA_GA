from lib.Test.Tester import *
from lib.Test.MultiTester import *
from lib.Utility.ConfigParser import *
from lib.Utility.CompareResults import *
import sys

def testOne(cp):
    t = Tester(cp)

    t.run()

def multiTest(cp):
    m = MultiTester(cp)

    m.generateMultOutput(cp.getSetting('OUTPUT_DIRECTORY'))

    cr = CompareResults(cp.getSetting('OUTPUT_DIRECTORY'))

    cr.plotAllOneGraph(int(cp.getSetting('MIN_ALPHABET_SIZE')),
        int(cp.getSetting('MAX_ALPHABET_SIZE')),
        int(cp.getSetting('MIN_EXAMPLES_PER_FILE')),
        int(cp.getSetting('MAX_EXAMPLES_PER_FILE')),
        int(cp.getSetting('FILES_TO_GENERATE')),)

# read in a configuration file from parameters and send to tester
if __name__ == '__main__':
    # create object to parse config file
    cp = ConfigParser()
    # parse the configuration file
    try:
        cp.parse(sys.argv[1])
        cfg = sys.argv[1]
    except:
        print "Need a config file"
        exit() # if one was not provided, exit

    if int(cp.getSetting('TEST_OPTION')) == 1: testOne(cp)

    elif int(cp.getSetting('TEST_OPTION')) == 2:  multiTest(cp)
