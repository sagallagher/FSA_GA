from DataParser import *
from Chromosome import *
from InitializePopulation import *
from Genotype import *
from Fitness import *
from Mutation import *
from Crossover import *
from GeneticAlgorithm import *
# main method
if __name__ == '__main__':
    dp = DataParser('test_data.txt')

    genotype = Genotype()

    ip = InitializePopulation(dp,2,2,4);
    f = Fitness(dp)
    c = Crossover()
    m = Mutation(dp)

    ga = GeneticAlgorithm(ip,f,c,m)

    ga.start()
