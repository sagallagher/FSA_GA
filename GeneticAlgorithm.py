from Genotype import *
class GeneticAlgorithm():
    def __init__(self, initialize_population, fitness, crossover, mutation):
        self.initialize_population = initialize_population
        self.fitness = initialize_population
        self.crossover = crossover
        self.mutation = mutation


    def start(self):
        genotype = Genotype()
        generation = 0
        a = 0
        self.initialize_population.start(genotype)
        while(True):
            print "fitness"
            a = input()
            self.fitness.start(genotype)

            if genotype.getMaxFitness() >= 1: break

            print 'mutation'
            self.mutation.start(genotype)

            print 'crossover'
            self.crossover.start(genotype)



            print generation,"\n******************************\n",genotype
            generation+=1
