
from Test.ConfigParser import *
from Test.Tester import *
import sys

# read in a configuration file from parameters and send to tester
if __name__ == '__main__':
    # create object to parse config file
    cp = ConfigParser()
    # parse the configuration file
    if not cp.parse(sys.argv[1]): exit()
    # send the configuration file to the tester so it can use the settings provided
    t = Tester(cp)
    print cp.settings

    # run the tests
    t.run()
