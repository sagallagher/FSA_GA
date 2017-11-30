from DataParser.DataParser import *
from GeneticAlgorithm.GeneticOperator.InitializePopulation.RandomInitializePopulation import *
from GeneticAlgorithm.GeneticOperator.Fitness.FSMHitRatioFitness import *
from GeneticAlgorithm.GeneticOperator.Crossover.RandomCrossover import *
from GeneticAlgorithm.GeneticOperator.Mutation.RandomTransitionMutation import *
from GeneticAlgorithm.Genotype import *
from GeneticAlgorithm.GeneticAlgorithm import *
from Test.LearningDataGenerator.RandomLearningDataGenerator import *

import os

class Tester():

    def __init__(self, config_parser):
    ################################################################################
                                # USER SETTINGS
    ################################################################################

        # generate random files?
        self.RANDOM_GEN = config_parser.getSetting('RANDOM_GEN').lower() == 'true'

        # file to output results in
        self.OUTPUT_FILE = str(config_parser.getSetting('OUTPUT_FILE'))

    ################################################################################
    # LEARNING DATA GENERATOR SETTINGS
    ################################################################################
        # prefix to place on numbered outputted files
        self.DIRECTORY = str(config_parser.getSetting('DIRECTORY'))
        # number of learning data sets to generate
        self.FILES_TO_GENERATE = int(config_parser.getSetting('FILES_TO_GENERATE'))
        # number of examples to include in each file
        self.EXAMPLES_PER_FILE = int(config_parser.getSetting('EXAMPLES_PER_FILE'))
        # the size of the alphabet to use
        self.ALPHABET_SIZE = int(config_parser.getSetting('ALPHABET_SIZE'))
        # minimum length of each example word
        self.MINIMUM_LENGTH = int(config_parser.getSetting('MINIMUM_LENGTH'))
        # maximum length of each example word
        self.MAXIMUM_LENGTH = int(config_parser.getSetting('MAXIMUM_LENGTH'))

    ################################################################################
    # GENETIC ALGORITHM SETTINGS
    ################################################################################
        # add another random individual to the population at this generation
        self.DIVERSITY_AT = int(config_parser.getSetting('DIVERSITY_AT'))
        # stop pursing current learning data set when there is a chromosome of this fitness
        self.THRESHOLD = float(config_parser.getSetting('THRESHOLD'))
        # generation to stop pursuing the current learning data set
        self.GIVE_UP = int(config_parser.getSetting('GIVE_UP'))
        # the number of randomly generated FSMs to include in the initial population
        self.POPULATION_SIZE = int(config_parser.getSetting('POPULATION_SIZE'))
        # the minimum number of states for each FSM
        self.MIN_STATES = int(config_parser.getSetting('MIN_STATES'))
        # the maximum number of states for each FSM
        self.MAX_STATES = int(config_parser.getSetting('MAX_STATES'))

        self.FILE_PREFIX = int(config_parser.getSetting('FILE_PREFIX'))

    # generate random files in the given directory
    def generateRandomFiles(self):
        #for the_file in os.listdir(self.DIRECTORY): os.unlink(os.path.join(self.DIRECTORY, the_file))
        # construct a RandomLearningGenator to generate random training datasets
        rlg = RandomLearningGenerator(self.DIRECTORY,self.FILE_PREFIX, self.FILES_TO_GENERATE,self.EXAMPLES_PER_FILE,
            self.ALPHABET_SIZE,self.MINIMUM_LENGTH,self.MAXIMUM_LENGTH)

        # use the object to generate the desired number of files with the given properties
        rlg.generateLearningData()

    # test one directory
    # return an array of the number of solutions checked for each file
    def testDirectory(self):

        solutions_checked = []

        f =  open(self.OUTPUT_FILE, 'w')

        for filename in os.listdir(self.DIRECTORY):
            # parse the training data set
            dp = DataParser(os.path.join(self.DIRECTORY, filename))
            dp.setAlphabetSize()
            # initialize genetic operators
            ip = RandomInitializePopulation(dp,self.POPULATION_SIZE,self.MIN_STATES,self.MAX_STATES);
            fitness = FSMHitRatioFitness(dp)
            c = RandomCrossover()
            m = RandomTransitionMutation(dp)
            # pass all genetic operators to genetic algorithm
            ga = GeneticAlgorithm(ip,fitness,c,m)

            # start the genetic algorithm
            (fsm,generation) = ga.start(self.DIVERSITY_AT,self.THRESHOLD,self.GIVE_UP)
            # output results to given output file

            f.write(filename+'\n')
            # display the number of solutions checked for each file in output
            f.write('Solutions Checked:\t'+str(generation)+'\n'+str(fsm)+'\n')
            # append the number of solutions checked in current file to array of solutions
            solutions_checked.append(generation)

        # write the array of solutions checked to the bottom of the file
        # this will make it easier to load in the data and compare two algorithms
        f.write(str(solutions_checked))
        # close the file
        f.close()
        # return the array of solutions checked
        return solutions_checked

    def run(self):
        # if RANDOM_GEN set to true in the config file, generate random files
        # at the directory provided in the config file
        if self.RANDOM_GEN: self.generateRandomFiles()
        # clear the output file
        self.testDirectory()
