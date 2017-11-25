
from Test.ConfigParser import *
from Test.Tester import *
import sys

# read in a configuration file from parameters and send to tester
if __name__ == '__main__':
    # create object to parse config file
    cp = ConfigParser()
    # parse the configuration file
    try: cp.parse(sys.argv[1])
    except:
        print "Need a config file"
        exit() # if one was not provided, exit
    # send the configuration file to the tester so it can use the settings provided
    t = Tester(cp)
    # run the tests
    t.run()
