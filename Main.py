from DataParser import *
from Chromosome import *
from InitializePopulation import *
from Genotype import *
from Fitness import *
from Mutation import *
from Crossover import *
# main method
if __name__ == '__main__':
    dp = DataParser('test_data.txt')

    ip = InitializePopulation(dp.alphabet_size,4,3,3);


    f = Fitness(ip.genotype, dp.learning_data, dp.alphabet_size)


    i = 0
    while(True):
        i+=1
        if f.genotype.getMaxFitness() >= 1: break

        m = Mutation(f.genotype, dp.alphabet_size)

        c = Crossover(m.genotype)

        f = Fitness(c.genotype, dp.learning_data, dp.alphabet_size)

    print f.genotype
    print "generations:\t", i
