from DataParser.DataParser import *
from InitializePopulation.RandomInitializePopulation import *
from Fitness.FSMHitRatioFitness import *
from Crossover.RandomCrossover import *
from Mutation.RandomTransitionMutation import *
from Genotype.Genotype import *
from GeneticAlgorithm.GeneticAlgorithm import *
from LearningDataGenerator.RandomLearningDataGenerator import *

import os

class Tester():

    def __init__(self, config_parser):
        self.cp = config_parser

    def run(self):

        ################################################################################
                                    # USER SETTINGS
        ################################################################################

            # generate random files?
            RANDOM_GEN = self.cp.getSetting('RANDOM_GEN').lower() == 'true'

            # file to output results in
            OUTPUT_FILE = str(self.cp.getSetting('OUTPUT_FILE'))

        ################################################################################
        # LEARNING DATA GENERATOR SETTINGS
        ################################################################################
            # prefix to place on numbered outputted files
            DIRECTORY = str(self.cp.getSetting('DIRECTORY'))
            # number of learning data sets to generate
            FILES_TO_GENERATE = int(self.cp.getSetting('FILES_TO_GENERATE'))
            # number of examples to include in each file
            EXAMPLES_PER_FILE = int(self.cp.getSetting('EXAMPLES_PER_FILE'))
            # the size of the alphabet to use
            ALPHABET_SIZE = int(self.cp.getSetting('ALPHABET_SIZE'))
            # minimum length of each example word
            MINIMUM_LENGTH = int(self.cp.getSetting('MINIMUM_LENGTH'))
            # maximum length of each example word
            MAXIMUM_LENGTH = int(self.cp.getSetting('MAXIMUM_LENGTH'))

        ################################################################################
        # GENETIC ALGORITHM SETTINGS
        ################################################################################
            # add another random individual to the population at this generation
            DIVERSITY_AT = int(self.cp.getSetting('DIVERSITY_AT'))
            # stop pursing current learning data set when there is a chromosome of this fitness
            THRESHOLD = float(self.cp.getSetting('THRESHOLD'))
            # generation to stop pursuing the current learning data set
            GIVE_UP = int(self.cp.getSetting('GIVE_UP'))
            # the number of randomly generated FSMs to include in the initial population
            POPULATION_SIZE = int(self.cp.getSetting('POPULATION_SIZE'))
            # the minimum number of states for each FSM
            MIN_STATES = int(self.cp.getSetting('MIN_STATES'))
            # the maximum number of states for each FSM
            MAX_STATES = int(self.cp.getSetting('MAX_STATES'))

        ################################################################################

        ################################################################################

        ################################################################################
                                    # END USER SETTINGS
        ################################################################################

        ################################################################################

        ################################################################################

            if RANDOM_GEN:
                # clear directory
                for the_file in os.listdir(DIRECTORY): os.unlink(os.path.join(DIRECTORY, the_file))

                rlg = RandomLearningGenerator(DIRECTORY,FILES_TO_GENERATE,EXAMPLES_PER_FILE,
                    ALPHABET_SIZE,MINIMUM_LENGTH,MAXIMUM_LENGTH)

                rlg.generateLearningData()

            # clear the output file
            f = open(OUTPUT_FILE, 'w').close()

            for filename in os.listdir(DIRECTORY):
                print "Parsing:\t", filename
                dp = DataParser(os.path.join(DIRECTORY, filename))
                dp.setAlphabetSize()


                ip = RandomInitializePopulation(dp,POPULATION_SIZE,MIN_STATES,MAX_STATES);
                fitness = FSMHitRatioFitness(dp)
                c = RandomCrossover()
                m = RandomTransitionMutation(dp)
                ga = GeneticAlgorithm(ip,fitness,c,m)


                (fsm,generation) = ga.start(DIVERSITY_AT,THRESHOLD,GIVE_UP)
                f =  open(OUTPUT_FILE, 'a')
                f.write(filename+'\n')
                f.write('Solutions Checked:\t'+str(generation)+'\n'+str(fsm)+'\n')
                f.close()
                print "Finished parsing:\t", filename
