# class to parse a config and store as a dictionary of settings
class ConfigParser():
    def __init__(self):
        self.settings = {}

    def parse(self,config_file):
        f = open(config_file,'r')

        for line in f:

            if len(line) <= 1 or line[0] == ' 'or line[0] == '#': pass

            else:
                split_line = line.split('=')

                try:
                    key = split_line[0]
                    value = split_line[1]
                    self.settings[key.replace(' ', '')] = value.replace(' ','').replace('\n','')
                except:
                    print "Could not parse configuration file", key
                    return -1


        f.close()

    def getSetting(self,key):
        try: return self.settings[key]
        except:
            print "setting cannot be found:\t", key
            return -1
