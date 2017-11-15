from Genotype import *
class GeneticAlgorithm():
    def __init__(self, initialize_population, fitness, crossover, mutation):
        self.initialize_population = initialize_population
        self.fitness = fitness
        self.crossover = crossover
        self.mutation = mutation


    def start(self):

        genotype = Genotype()
        generation = 0
        a = 0
        self.initialize_population.start(genotype)
        self.fitness.start(genotype)
        while(True):

            if generation%1000 == 0: print "generation:\t", generation
            self.fitness.start(genotype)

            if genotype.getMaxFitness() >= 1: break

            self.mutation.start(genotype)


            self.crossover.start(genotype)

            generation+=1

        print "final generation:\t", generation
        return genotype
