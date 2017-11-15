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


            self.fitness.start(genotype)

            if genotype.getMaxFitness() >= 1: break

            self.mutation.start(genotype)


            self.crossover.start(genotype)

            print generation,"\n******************************\n",genotype
            generation+=1

        return genotype
