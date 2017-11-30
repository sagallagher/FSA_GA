class DataParser():

    # constructor
    def __init__(self, data_file):
        self.data_file = data_file
        self.learning_data = {}
        self.alphabet_size = 0

        self.readDataFile()

    # string respresentation of data_matrix
    def __str__(self):
        result = ''

        for key in self.learning_data:
            result += (('%1s\t|\t%5s') % (key,self.learning_data[key]))

        return result

    def setAlphabetSize(self):
        max_int = 0

        for key in self.learning_data:
            key = key.replace('\n','').split(' ')

            for char in key:
                if char is not '' and int(char) > max_int:
                        max_int = int(char)

        self.alphabet_size = max_int+1



    # read the data file into data_matrix
    def readDataFile(self):

        with open(self.data_file, 'r') as f:
            for line in f:
                split_line = line.split(':')
                self.learning_data[split_line[0]] = split_line[1]
        self.setAlphabetSize()


    # return data_matrix
    def getLearningData(self): return self.learning_data
