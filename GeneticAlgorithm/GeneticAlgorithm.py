from Genotype.Genotype import *

class GeneticAlgorithm():
    def __init__(self, initialize_population, fitness, crossover, mutation):
        self.initialize_population = initialize_population
        self.fitness = fitness
        self.crossover = crossover
        self.mutation = mutation


    def start(self, introduce_diversity_at, threshold, give_up_at):

        geno = Genotype()
        generation = 1
        restart_count = 1
        self.initialize_population.start(geno)
        self.fitness.start(geno)
        count = 0
        while(True):
            '''
            If N generations pass without progress to the overall fitness of the
            genotype, introduce diversity
            '''

            if generation >= give_up_at: break
            # if we exceed N generations, introduce random chromosomes to the genotype
            if generation > introduce_diversity_at*restart_count:
                self.initialize_population.introduceDiversity(geno)
                restart_count += 1

            if generation%1000 == 0: print "generation:\t", generation

            self.fitness.start(geno)
            if geno.getMaxFitness() >= threshold: break

            self.mutation.start(geno)

            self.crossover.start(geno)

            generation+=1
            # track how many solutions we have checked
            count+=len(geno.chromosomes)


        if generation >= give_up_at: count = -count

        return geno.getMostFit(), count
