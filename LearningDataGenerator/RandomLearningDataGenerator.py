from random import randint

class RandomLearningGenerator():

    def __init__(self, directory, file_prefix,files_to_generate, examples_per_file,
        alphabet_size, min_word_length, max_word_length):
            self.files_to_generate = files_to_generate
            self.examples_per_file = examples_per_file
            self.alphabet_size = alphabet_size
            self.file_prefix = str(file_prefix)
            self.min_word_length = min_word_length
            self.max_word_length = max_word_length
            self.directory = directory

    def generateOneFile(self, file_name):
        with open(file_name, 'w') as f:

            for example_number in xrange(self.examples_per_file):
                key = ''
                value = 0
                for chracter_index in xrange(randint(self.min_word_length,self.max_word_length)):

                        key += (str(randint(0,self.alphabet_size-1))+' ')

                f.write(key[:len(key)-1] + ':' + str(randint(0,1)) + '\n')

    def generateLearningData(self):
        for file_number in xrange(self.files_to_generate):
            self.generateOneFile(self.directory+self.file_prefix+str(file_number)+'.txt')
