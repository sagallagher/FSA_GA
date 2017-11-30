# class to parse a config and store as a dictionary of settings
class ConfigParser():
    def __init__(self):
        self.settings = {}

    def parse(self,config_file):
        try: f = open(config_file,'r')
        except:
            print "Could not find configuration file"
            return False

        for line in f:
            # skip empty or commented lines
            # comments start with #
            if len(line) <= 1 or line[0] == ' 'or line[0] == '#': pass

            else:
                split_line = line.split('=')

                try:
                    key = split_line[0]
                    value = split_line[1]
                    # strip white space key and value and strip new line from char from value
                    self.settings[key.replace(' ', '')] = value.replace(' ','').replace('\n','')
                except:
                    print 'Could not parse key:\t', key
                    return False


        f.close()
        return True

    def getSetting(self,key):
        try: return self.settings[key]
        except:
            print "setting cannot be found:\t", key
            return -1
