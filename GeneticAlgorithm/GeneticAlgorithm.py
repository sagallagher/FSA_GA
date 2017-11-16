from Genotype.Genotype import *

class GeneticAlgorithm():
    def __init__(self, initialize_population, fitness, crossover, mutation):
        self.initialize_population = initialize_population
        self.fitness = fitness
        self.crossover = crossover
        self.mutation = mutation


    def start(self, introduce_diversity_at):

        geno = Genotype()
        generation = 1
        restart_count = 1
        self.initialize_population.start(geno)
        self.fitness.start(geno)

        while(True):
            '''
            If N generations pass without progress to the overall fitness of the
            genotype, introduce diversity
            '''
            # if we exceed N generations, introduce random chromosomes to the genotype
            if generation > introduce_diversity_at*restart_count:
                self.initialize_population.start(geno)
                restart_count += 1

            if generation%10000 == 0: print "generation:\t", generation,'\n',geno

            self.fitness.start(geno)

            if geno.getMaxFitness() >= 1: break

            self.mutation.start(geno)

            self.crossover.start(geno)

            generation+=1



        print "final generation:\t", generation
        return geno
