from DataParser.DataParser import *
from InitializePopulation.RandomInitializePopulation import *
from Fitness.FSMHitRatioFitness import *
from Crossover.RandomCrossover import *
from Mutation.RandomTransitionMutation import *
from Genotype.Genotype import *
from GeneticAlgorithm.GeneticAlgorithm import *
from LearningDataGenerator.RandomLearningDataGenerator import *
import os



# main method
if __name__ == '__main__':

################################################################################
                            # USER SETTINGS
################################################################################

    # file to output results in
    OUTPUT_FILE = 'output.txt'

################################################################################
# LEARNING DATA GENERATOR SETTINGS
################################################################################
    # prefix to place on numbered outputted files
    FILE_PREFIX = 'Data/Dataset1/'
    # number of learning data sets to generate
    FILES_TO_GENERATE = 100
    # number of examples to include in each file
    EXAMPLES_PER_FILE = 20
    # the size of the alphabet to use
    ALPHABET_SIZE = 2
    # minimum length of each example word
    MINIMUM_LENGTH = 0
    # maximum length of each example word
    MAXIMUM_LENGTH = 10

################################################################################
# GENETIC ALGORITHM SETTINGS
################################################################################
    # add another random individual to the population at this generation
    DIVERSITY_AT = 1000
    # stop pursing current learning data set when there is a chromosome of this fitness
    THRESHOLD = .9
    # generation to stop pursuing the current learning data set
    GIVE_UP = 10000
    # the number of randomly generated FSMs to include in the initial population
    POPULATION_SIZE = 20
    # the minimum number of states for each FSM
    MIN_STATES = 2
    # the maximum number of states for each FSM
    MAX_STATES = 10

################################################################################

################################################################################

################################################################################
                            # END USER SETTINGS
################################################################################

################################################################################

################################################################################



















    rlg = RandomLearningGenerator(FILE_PREFIX,FILES_TO_GENERATE,EXAMPLES_PER_FILE,
        ALPHABET_SIZE,MINIMUM_LENGTH,MAXIMUM_LENGTH)

    rlg.generateLearningData()
    # loop through all learning data sets in a directory
    #testAll(FILE_PREFIX,DIVERSITY_AT, THRESHOLD, GIVE_UP,POPULATION_SIZE,MIN_STATES,MAX_STATES)
    #testOne("Data/test_data.txt")
    with open('output.txt','w') as f:
        for filename in os.listdir(FILE_PREFIX):
            print "Parsing:\t", filename
            dp = DataParser(os.path.join(FILE_PREFIX, filename))
            dp.setAlphabetSize()


            ip = RandomInitializePopulation(dp,POPULATION_SIZE,MIN_STATES,MAX_STATES);
            fitness = FSMHitRatioFitness(dp)
            c = RandomCrossover()
            m = RandomTransitionMutation(dp)
            ga = GeneticAlgorithm(ip,fitness,c,m)


            (fsm,generation) = ga.start(DIVERSITY_AT,THRESHOLD,GIVE_UP)
            f.write(filename+'\n')
            f.write('Solutions Checked:\t'+str(generation)+'\n'+str(fsm)+'\n')
            print "Finished parsing:\t", filename
