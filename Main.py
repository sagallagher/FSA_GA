from DataParser.DataParser import *
from InitializePopulation.RandomInitializePopulation import *
from Fitness.FSMHitRatioFitness import *
from Crossover.RandomCrossover import *
from Mutation.RandomTransitionMutation import *
from Genotype.Genotype import *
from GeneticAlgorithm.GeneticAlgorithm import *

# main method
if __name__ == '__main__':
    dp = DataParser('Data/test_data.txt')
    dp.setAlphabetSize()


    ip = RandomInitializePopulation(dp,3,2,2);
    f = FSMHitRatioFitness(dp)
    c = RandomCrossover()
    m = RandomTransitionMutation(dp)
    ga = GeneticAlgorithm(ip,f,c,m)

    print ga.start(1000)
