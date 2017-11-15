from Genotype.Genotype import *
class GeneticAlgorithm():
    def __init__(self, initialize_population, fitness, crossover, mutation):
        self.initialize_population = initialize_population
        self.fitness = fitness
        self.crossover = crossover
        self.mutation = mutation


    def start(self):

        geno = Genotype()
        generation = 1

        self.initialize_population.start(geno)
        self.fitness.start(geno)

        while(True):

            if generation%1000 == 0: print "generation:\t", generation
            self.fitness.start(geno)

            if geno.getMaxFitness() >= 1: break

            self.mutation.start(geno)


            self.crossover.start(geno)

            generation+=1

        print "final generation:\t", generation
        return geno
