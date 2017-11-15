from DataParser import *
from InitializePopulation import *
from Fitness import *
from Mutation import *
from Crossover import *
from GeneticAlgorithm import *
# main method
if __name__ == '__main__':
    dp = DataParser('test_data.txt')

    genotype = Genotype()

    ip = InitializePopulation(dp,5,2,2);
    f = Fitness(dp)
    c = Crossover()
    m = Mutation(dp)

    ga = GeneticAlgorithm(ip,f,c,m)

    print ga.start()
