from DataParser.DataParser import *
from InitializePopulation.RandomInitializePopulation import *
from Fitness.FSMHitRatioFitness import *
from Crossover.RandomCrossover import *
from Mutation.RandomTransitionMutation import *
from Genotype.Genotype import *
from GeneticAlgorithm.GeneticAlgorithm import *
from LearningDataGenerator.RandomLearningDataGenerator import *
from Test.ConfigParser import *
from Test.RandomTester import *
import os



# main method
if __name__ == '__main__':

    cp = ConfigParser()
    cp.parse('config.txt')
    rt = RandomTester(cp)
    print cp.getSetting('MIN_STATES')
    rt.run()
